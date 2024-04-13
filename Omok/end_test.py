def right_case(point, points):
    col = point[0]
    row = point[1]
    
    for i in range(1, 5):
        if ( (col, row + i) not in points):
            return False 
    return True


def down_case(point, points):
    col = point[0]
    row = point[1]
    
    for i in range(1, 5):
        if ( (col + i, row) not in points):
            return False
    return True


def right_down_case(point, points):
    col = point[0]
    row = point[1]
    
    for i in range(1, 5):
        if ( (col + i, row + i) not in points):
            return False 
    return True


def left_down_case(point, points):
    col = point[0]
    row = point[1]
    
    for i in range(1, 5):
        if ( ( col + i, row - i) not in points):
            return False
    return True


def state_func(game): # 해당 game 이 종료 되었는지 아닌지를 판단
    if ( len(game["b"]) == len(game["w"])): # 마지막에 w 가 둠
        color = "w"
    else:
        color = "b" # 마지막에 b 가 둠

    points = game[color]
    
    for i in points:
        if ( right_case(i, points) ):
            return "end", color
        if ( down_case(i, points) ):
            return "end", color
        if ( right_down_case(i, points) ):
            return "end", color
        if ( left_down_case(i, points) ):
            return "end", color
    return "during", color
