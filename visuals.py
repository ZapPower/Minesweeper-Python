letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

def linevisual(columns):
    letcount = 0
    linevisual = "[0] "
    for i in range(columns):
        linevisual += "["+letters[letcount]+"] "
        letcount += 1
    linevisual += "[0]"
    return linevisual