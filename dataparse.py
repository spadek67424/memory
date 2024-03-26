import numpy as np
TotalLossgreedy = 0
def greedy_algorithm(func, process_list):
    overlaploss = list()
    for i in process_list:
        for j in process_list:
            notUnionProcess = list()
            if(i == j):
                continue
            array1=list()
            array2=list()
            for k in process_list[i][0].split(", "):
                array1.append(k)
            for k in process_list[j][0].split(", "):
                array2.append(k)
            for k in array1:
                if k not in array2:
                    notUnionProcess.append(k)
            for k in array2:
                if k not in array1:
                    notUnionProcess.append(k)
            overlaploss.append((i,j, len(notUnionProcess)))
    np.random.shuffle(overlaploss)
    print(overlaploss)
    minloss = np.iinfo(np.int32).max
    target = 0
    ## find the minimum
    global TotalLossgreedy
    TotalLossgreedy = 0
    functionstring = list()
    #### First round of greedy algorithm.
    minloss = np.iinfo(np.int32).max
    for i in overlaploss:
        if(i[2] < minloss):
            target = i
            minloss = i[2]
    TotalLossgreedy +=minloss
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
    while(len(overlaploss) > 0):  
        backuplist = list()  
        for i in overlaploss:
            if i[0]== nextindex:
                backuplist.append(i)
        minloss = np.iinfo(np.int32).max
        for i in backuplist:
            if(i[2] < minloss):
                target = i
                minloss = i[2]
        TotalLossgreedy +=minloss
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


def greedy_combined_algorithm(func, process_list):
    overlaploss = list()
    function_set =dict()
    for i in process_list:
        if process_list[i][0] in function_set.keys():
            if i not in function_set[process_list[i][0]]:
                function_set[process_list[i][0]].append(i)
        else:
            function_set[process_list[i][0]] = list()
            function_set[process_list[i][0]].append(i)
    for i in function_set.keys():
        print(i)
        print(function_set[i])
    for i in function_set:
        for  j in function_set:
            if i == j:
                continue
            notUnionProcess = list()
            array1=list()
            array2=list()
            for k in i.split(", "):
                array1.append(k)
            for k in j.split(", "):
                array2.append(k)
            for k in array1:
                if k not in array2:
                    notUnionProcess.append(k)
            for k in array2:
                if k not in array1:
                    notUnionProcess.append(k)
            overlaploss.append((function_set[i],function_set[j], len(notUnionProcess)))
    np.random.shuffle(overlaploss)
    print(len(overlaploss))
    minloss = np.iinfo(np.int32).max
    target = 0
    ## find the minimum
    global TotalLossgreedy
    TotalLossgreedy = 0
    functionstring = list()
    #### First round of greedy algorithm.
    minloss = np.iinfo(np.int32).max
    for i in overlaploss:
        if(i[2] < minloss):
            target = i
            minloss = i[2]
    TotalLossgreedy +=minloss
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
    while(len(overlaploss) > 0):  
        backuplist = list()  
        for i in overlaploss:
            if i[0]== nextindex:
                backuplist.append(i)
        minloss = np.iinfo(np.int32).max
        for i in backuplist:
            if(i[2] < minloss):
                target = i
                minloss = i[2]
        TotalLossgreedy +=minloss
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

 
def readsize():
    with open('./data/symbol_size.txt', 'r') as days_file:
        size_dict = dict()
        for line in days_file:
            size, symbol = line.split(" ")
            size_dict[symbol] = size
    return size_dict
def readfile():
    process_list = dict()
    with open('./data/sym_dep_info.txt', 'r') as days_file:
        for line in days_file:
            line = line.split(":")[1]
            func, left = line.split("is")
            apps, libs = left.split("and")
            token = apps.split("{")
            token = token[1].split("}")
            for process in token[:-1]:
                if func in process_list.keys():
                    process_list[func].append(str(process))
                else:
                    process_list[func] = list()
                    process_list[func].append(str(process))
    return process_list
if __name__ == "__main__":   
    func = readsize() 
    process_list = readfile()
    greedy_algorithm(func, process_list)
    print(TotalLossgreedy)
    greedy_combined_algorithm(func, process_list)
    print(TotalLossgreedy)
    
    
    