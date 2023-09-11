import random
def makeClearBoard(columns, rows):
    arr = []
    for i in range(columns):
        cols = []
        for j in range(rows):
            cols.append(" ")
        arr.append(cols)
    return arr

def findBoundingNum(arr, center):
    #find num of bombs about index
    bCount = 0
    if (center[1] > 0):
        if (arr[center[0]][center[1] - 1] == 1): bCount+=1;
    if (center[0] != 0):
        if (arr[center[0] - 1][center[1]] == 1): bCount+=1;
        if (center[1] > 0):
            if (arr[center[0] - 1][center[1] - 1] == 1): bCount+=1;
        if (center[1] < len(arr[center[0]]) - 1 and arr[center[0] - 1][center[1] + 1] == 1): bCount+=1;
    if (center[0] != len(arr) - 1):
        if (center[1] > 0):
            if (arr[center[0] + 1][center[1] - 1] == 1): bCount+=1;
        if (arr[center[0] + 1][center[1]] == 1): bCount+=1;
        if (center[1] < len(arr[center[0]]) - 1 and arr[center[0] + 1][center[1] + 1] == 1): bCount+=1;
    if (center[1] < len(arr[center[0]]) - 1 and arr[center[0]][center[1] + 1] == 1): bCount+=1;
    if bCount == 0:
        return " "
    return bCount

def makeBoard(columns,rows,bombpct):
    arr = []
    bombs = []
    for i in range(columns):
        cols = []
        for j in range(rows):
            if random.randint(0,100) <= bombpct:
                cols.append(1)
                bombs.append([i, j])
            else:
                cols.append(0)
        arr.append(cols)
    
    for i in range(columns):
        for j in range(rows):
            if (arr[i][j] == 1):
                continue
            else:
                arr[i][j] = "["+str(findBoundingNum(arr, [i,j]))+"]"
    return arr, bombs

def startup():
    columns = int(input("How many columns?: "))
    rows = int(input("How many rows?: "))
    percentbomb = int(input("Enter bomb occurance percentage: "))
    
    return columns, rows, percentbomb