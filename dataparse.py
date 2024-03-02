def readfile():
    with open('./data/sym_dep_info.txt', 'r') as days_file:
        for line in days_file:
            line = line.split(":")[1]
            func, left = line.split("is")
            print(func)
            apps, libs = left.split("and")
            token = apps.split("'")
            print(token[1])
            token = libs.split("'")
            print(token[1])            
if __name__ == "__main__":    
    readfile()