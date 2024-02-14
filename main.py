import numpy as np
import random

### input data set
FunctSet = 7
TotalProcess = 10
ProcessinEachSet = 5
MaxofFunctionsize = 8192
MaxProcessLoss = 50
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
    naive_algorithm(func, processlist, processLoss)
    print(TotalLoss)