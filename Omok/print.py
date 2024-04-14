num = -1
board = [["x  ", "A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ", "I ", "J ", "K ", "L ", "M ", "N ", "O ", "P ", "Q ", "R ", "S "]]
for i in range(1, 20):
    if(i<10):
        board.append([str(i) + "  "])
    else:
        board.append([str(i) + " "])
    for j in range(19):
        board[i].append("- ")


def draw(point): 
    global board, num
    
    if(point == "init"):
        num = num * (-1)
    else:
        col, row = point

        if(num == -1):
            board[col][row] = "B "
        elif(num == 1):
            board[col][row] = "W "
    num = num * (-1)
    
    for i in board:
        str = ""
        for j in range(len(i)):
            str += i[j]
        print(str)
    print("\n")
    