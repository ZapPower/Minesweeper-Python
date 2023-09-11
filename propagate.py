def surroundCheck(clearBoard, board, center):
    cArr = []
    
    if (center[1] > 0):
        #TOP
        if (board[center[0]][center[1] - 1] != 1 and clearBoard[center[0]][center[1] - 1] == " "): 
            cArr.append([center[0], center[1] - 1]);
    if (center[0] != 0):
        #LEFT
        if (board[center[0] - 1][center[1]] != 1 and clearBoard[center[0] - 1][center[1]] == " "): 
            cArr.append([center[0] - 1, center[1]]);
        #TOPLEFT
        if (center[1] > 0):
            if (board[center[0] - 1][center[1] - 1] != 1 and clearBoard[center[0] - 1][center[1] - 1] == " "): 
                cArr.append([center[0] - 1, center[1] - 1]);
        #BOTTOMLEFT
        if (center[1] < len(board[center[0]]) - 1 and board[center[0] - 1][center[1] + 1] != 1 and clearBoard[center[0] - 1][center[1] + 1] == " "): 
            cArr.append([center[0] - 1, center[1] + 1]);
    if (center[0] != len(board) - 1):
        #TOPRIGHT
        if (center[1] > 0):
            if (board[center[0] + 1][center[1] - 1] != 1 and clearBoard[center[0] + 1][center[1] - 1] == " "): 
                cArr.append([center[0] + 1, center[1] - 1]);
        #RIGHT
        if (board[center[0] + 1][center[1]] != 1 and clearBoard[center[0] + 1][center[1]] == " "): 
            cArr.append([center[0] + 1, center[1]]);
        #BOTTOMRIGHT
        if (center[1] < len(board[center[0]]) - 1 and board[center[0] + 1][center[1] + 1] != 1 and clearBoard[center[0] + 1][center[1] + 1] == " "): 
            cArr.append([center[0] + 1, center[1] + 1]);
    #BOTTOM
    if (center[1] < len(board[center[0]]) - 1 and board[center[0]][center[1] + 1] != 1 and clearBoard[center[0]][center[1] + 1] == " "): 
        cArr.append([center[0], center[1] + 1]);
    
    return cArr

def propagateSelection(clearBoard, board, select):
    #clear selection
    newClearBoard = clearBoard
    if board[select[0]][select[1]] == 1:
        return -1
    newClearBoard[select[0]][select[1]] = "C"
    if (board[select[0]][select[1]] != "[ ]"):
        return newClearBoard
    
    #propagate through matrix
    clearArr = surroundCheck(clearBoard, board, select)
    while len(clearArr) > 0:
        replaceArr = []
        for point in clearArr:
            newClearBoard[point[0]][point[1]] = "C"
        #needs to be separated to prevent repetition in array
        for point in clearArr:
            for newpoint in surroundCheck(clearBoard, board, point):
                newClearBoard[newpoint[0]][newpoint[1]] = "C"
                #only add to next sweep if new point is empty
                if (board[newpoint[0]][newpoint[1]] == "[ ]"):
                    replaceArr.append(newpoint)
        clearArr = replaceArr
    
    return newClearBoard