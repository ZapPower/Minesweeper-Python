from startup import *
from visuals import *
from propagate import *

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

while True:
    print("Welcome to Minesweeper Python! Enter 'start' to start")
    begin = input(": ")
    if begin.lower() == "start":
        break;

cols, rows, bpct = startup()
board, bombs = makeBoard(cols, rows, bpct)
clearBoard = makeClearBoard(cols, rows)
print("---------------------------------------------------\n\n")

flagsUsed = len(bombs)
flagsPlaced = []

def printBoard():
    print(linevisual(cols))
    for j in range(rows):
        currentLine = ""
        for i in range(cols + 2):
            if (i == 0 or i == cols + 1):
                currentLine += "["+letters[j]+"] "
            else:
                if (clearBoard[i - 1][j] == "C"):
                    currentLine += str(board[i - 1][j]) + " "
                elif (clearBoard[i - 1][j] == "F"):
                    currentLine += "[F] "
                else:
                    currentLine += "[x] "
        print(currentLine)
    print(linevisual(cols))

def printLowerBoard():
    #FOR DEBUGGING ONLY (kind of)
    for i in range(rows):
        currentLine = ""
        for j in range(cols):
            if (board[j][i] == 1):
                currentLine += "[B] "
            else:
                currentLine += str(board[j][i]) + " "
        print(currentLine)
        
def printClearBoard():
    #FOR DEBUGGING ONLY
    for i in range(rows):
        currentLine = ""
        for j in range(cols):
            currentLine += "["+clearBoard[j][i]+"] "
        print(currentLine)
        
def restartGame():
    global cols, rows, bpct
    cols, rows, bpct = startup()
    global board, bombs
    board, bombs = makeBoard(cols, rows, bpct)
    global clearBoard
    clearBoard = makeClearBoard(cols, rows)
    global flagsUsed
    flagsUsed = len(bombs)
    global flagsPlaced
    flagsPlaced = []
    print("---------------------------------------------------\n\n")

while True:
    #MAIN GAME LOOP
    printBoard()
    print("Commands: Flag, Select, Restart (Flags: "+str(flagsUsed)+")")
    cli = input(": ").lower()
    cli = cli.split()
    if (cli[0] == "select"):
        if (clearBoard[letters.find(cli[1].upper())][letters.find(cli[2].upper())] == "F"):
            continue
        newClearBoard = propagateSelection(clearBoard, board, [letters.find(cli[1].upper()), letters.find(cli[2].upper())])
        if (newClearBoard == -1):
            print("Bomb!")
            for i in range(cols):
                for j in range(rows):
                    clearBoard[i][j] = "C"
            printLowerBoard()
            restartGame()
            continue
        clearBoard = newClearBoard
    elif (cli[0] == "flag"):
        sel = [letters.find(cli[1].upper()), letters.find(cli[2].upper())]
        if (clearBoard[sel[0]][sel[1]] == "F"):
            clearBoard[sel[0]][sel[1]] = " "
            flagsUsed += 1
            flagsPlaced.remove([sel[0], sel[1]])
        elif (clearBoard[sel[0]][sel[1]] != "C" and flagsUsed > 0):
            clearBoard[sel[0]][sel[1]] = "F"
            flagsUsed -= 1
            flagsPlaced.append([sel[0], sel[1]])
            if (sorted(flagsPlaced) == sorted(bombs)):
                print("You Win!")
                printLowerBoard()
                restartGame()
    elif (cli[0] == "restart"):
        restartGame()
    elif (cli[0] == "showlowerboard"):
        printLowerBoard()