import numpy as np
import random

### input data set
FunctSet = 7
TotalProcess = 10
ProcessinEachSet = 5
MaxofFunctionsize = 8192
MaxProcessLoss = 30
### memory
Page_Size = 4096
Page_Number = 30
MemorySize = Page_Size * Page_Number
TotalLoss = np.iinfo(np.int32).max
##########################
## iterate all the possible

def calculateLoss(Index, func, processlist, processLoss):
    size = func[Index[0]]
    previndex = Index[0]
    Loss = 0
    for i in Index[1:]:
        if(size % Page_Size != 0):
            size += func[i]
            notUnionProcess =np.setxor1d(processlist[previndex], processlist[i])
            previndex = i
            print(notUnionProcess)
            for j in notUnionProcess:
                Loss += processLoss[j]
    return Loss
def permute(Index, l, r, func, processlist, processLoss):
    global TotalLoss
    if(l == r):
        output = calculateLoss(Index, func, processlist, processLoss)
        if(TotalLoss > output):
            TotalLoss = output
            with open("output.txt", "a") as f:
                print(TotalLoss, file=f)
                print(Index, file=f)
                print(func, file=f)
                print(processlist, file=f)
                print(processLoss, file=f)
    else:
        for i in range(l, r):
            Index[l], Index[i] = Index[i], Index[l]
            permute(Index, l+1, r, func, processlist, processLoss)
            Index[l], Index[i] = Index[i], Index[l]

def naive_algorithm(func, processlist, processLoss):
    Index = np.arange(0, FunctSet)
    permute(Index, 0, FunctSet, func, processlist, processLoss)
 
def greedy_algorithm(func, processlist, processLoss):
    complimentary_list=list()
    previndex = 0
    notUnionProcess = list()
    for i in range(0, len(processlist)):
        for j in range(0, len(processlist)):
            if(i == j):
                continue
            notUnionProcess.append((i, j, np.setxor1d(processlist[i], processlist[j])))
    overlaploss = list()
    for i in notUnionProcess:
        Loss = 0
        for j in i[2]:
            Loss += processLoss[j]
        overlaploss.append((i[0], i[1], Loss))
    np.random.shuffle(overlaploss) 
    minloss = np.iinfo(np.int32).max
    target = 0
    ## find the minimum
    global TotalLoss
    TotalLoss = 0
    functionstring = list()
    #### First round of greedy algorithm.
    minloss = np.iinfo(np.int32).max
    print(overlaploss)
    for i in overlaploss:
        if(i[2] < minloss):
            target = i
            minloss = i[2]
    TotalLoss +=minloss
    removeindex = target[0]
    nextindex = target[1]
    functionstring.append(removeindex)
    backuplist = list()
    for i in overlaploss:
        if i[0] == removeindex or i[1] == removeindex:
            continue
        backuplist.append(i)
    overlaploss = backuplist
    #######
    while(len(functionstring) < FunctSet - 1):  
        backuplist = list()  
        for i in overlaploss:
            if i[0]== nextindex:
                backuplist.append(i)
        print(backuplist)
        minloss = np.iinfo(np.int32).max
        for i in backuplist:
            if(i[2] < minloss):
                target = i
                minloss = i[2]
        TotalLoss +=minloss
        removeindex = target[0]
        nextindex = target[1]
        functionstring.append(removeindex)
        backuplist = list() 
        for i in overlaploss:
            if i[0] == removeindex or i[1] == removeindex:
                continue
            backuplist.append(i)
        overlaploss = backuplist
    functionstring.append(nextindex)
    print(functionstring)
    ########
##########################    
 # @Func = each function set
 # @Processlist = each function set mapping to the process list
 # @processLoss = each process Loss.
###
def data_init():
    func = list()
    processlist = list()
    processLoss = list()
    for i in range(TotalProcess):
        processLoss.append(np.random.randint(1,MaxProcessLoss))
        
    for i in range(FunctSet):
        func.append(np.random.randint(1,MaxofFunctionsize))
        processlist.append(random.sample(range(0,TotalProcess), ProcessinEachSet))
    return func,processlist, processLoss
if __name__ == "__main__":
    func, processlist, processLoss = data_init()
    #naive_algorithm(func, processlist, processLoss)
    greedy_algorithm(func, processlist, processLoss)
    print(TotalLoss)