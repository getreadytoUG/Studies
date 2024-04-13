import const

outbounds = const.OUTBOUNDS

def evaluate(game, color): # 현재 게임의 우열을 결정하는 heuristic func
    if ( color == "b" ):
        computer = "b"
        player = "w"
    else:
        computer = "w"
        player = "b"
    
    evaluation_score = two_stone_one_block(game, computer, player) + two_stone_no_block(game, computer, player) + three_stone_one_block(game, computer, player) + three_stone_no_block(game, computer, player) + four_stone_two_block(game, computer, player) + four_stone_one_block(game, computer, player) + four_stone_no_block(game, computer, player) + five_stone(game, computer, player)
    
    opposite_score = two_stone_one_block(game, player, computer) + two_stone_no_block(game, player, computer) + three_stone_one_block(game, player, computer) + three_stone_no_block(game, player, computer) + four_stone_two_block(game, player, computer) + four_stone_one_block(game, player, computer) + four_stone_no_block(game, player, computer) + five_stone(game, player, computer)

    search_score = evaluation_score - 1.5 * opposite_score
    
    return search_score


def two_stone_one_block(game, target, opposite): # 연속된 두 돌과 막은 돌 하나
    global outbounds
    all_points = game[target] + game[opposite] + outbounds
    block_points = outbounds + game[opposite]
    score = 0
    
    for (col, row) in game[target]:
        # noblock + target + target + opposite
        if ((col, row+1) in game[target]) and ((col, row+2) in block_points) and ((col, row-1) not in all_points):
            score += 1
            
        # opposite + target + target + noblock
        elif ((col, row+1) in game[target]) and ((col, row+2) not in all_points) and ((col, row-1) in block_points):
            score += 1
            
        
        # noblock +
        # target +
        # target +
        # opposite
        if ((col+1, row) in game[target]) and ((col+2, row) in block_points) and ((col-1, row) not in all_points):
            score += 1
            
        # noblock +
        # target +
        # target +
        # opposite             
        elif ((col+1, row) in game[target]) and ((col+2, row) not in all_points) and ((col-1, row) in block_points):
            score += 1
            
        
        # noblock +
        #           target + 
        #                       target +
        #                                   opposite
        if ((col+1, row+1) in game[target]) and ((col+2, row+2) in block_points) and ((col-1, row-1) not in all_points):
            score += 1
            
        # opposite +
        #           target + 
        #                       target +
        #                                   noblock
        elif((col+1, row+1) in game[target]) and ((col+2, row+2) not in all_points) and ((col-1, row-1) in block_points):
            score += 1
            
            
        #                                 + noblock
        #                     + target 
        #         + target  
        # opposite 
        if((col+1, row-1) in game[target]) and ((col+2, row-2) in block_points) and ((col-1, row+1) not in all_points):
            score += 1
            
        #                                 + opposite
        #                     + target 
        #         + target  
        # noblock 
        elif((col+1, row-1) in game[target]) and ((col+2, row-2) not in all_points) and ((col-1, row+1) in block_points):
            score += 1
            
                
    return score 
        

def two_stone_no_block(game, target, opposite): # 연속된 두 돌과 막은 돌 없음
    global outbounds
    all_points = game[target] + game[opposite] + outbounds
    block_points = outbounds + game[opposite]
    score = 0
    
    for (col, row) in game[target]:
        # noblock + target + target + noblock
        if ((col, row+1) in game[target]) and ((col, row+2) not in all_points) and ((col, row-1) not in all_points):
            score += 3
            
        # noblock +
        # target + 
        # target + 
        # noblock 
        if ((col+1, row) in game[target]) and ((col+2, row) not in all_points) and ((col-1, row) not in all_points):
            score += 3
            
            
        # noblock +
        #           target +
        #                       target +
        #                                   noblock
        if ((col+1, row+1) in game[target]) and ((col+2, row+2) not in all_points) and ((col-1, row-1) not in all_points):
            score += 3
            
            
        #                                 + noblock
        #                     + target 
        #         + target 
        # noblock 
        if ((col+1, row-1) in game[target]) and ((col+2, row-2) not in all_points) and ((col-1, row+1) not in all_points):
            score += 3
            
    
    return score

        
def three_stone_one_block(game, target, opposite): # 연속된 세 돌과 막은 돌 하나
    global outbounds
    all_points = game[target] + game[opposite] + outbounds
    block_points = outbounds + game[opposite]
    score = 0
    
    for (col, row) in game[target]:
        # noblock + target + target + target + opposite
        if ((col, row+1) in game[target]) and ((col, row+2) in game[target]) and ((col, row+3) in block_points) and ((col, row-1) not in all_points):
            score += 5
            
        # opposite + target + target + target + noblock
        elif ((col, row+1) in game[target]) and ((col, row+2) in game[target]) and ((col, row+3) not in all_points) and ((col, row-1) in block_points):
            score += 5
            
        
        # noblock +
        # target +
        # target +
        # target +
        # opposite
        if ((col+1, row) in game[target]) and ((col+2, row) in game[target]) and ((col+3, row) in block_points) and ((col-1, row) not in all_points):
            score += 5
            
        # noblock +
        # target +
        # target +
        # target +
        # opposite             
        elif ((col+1, row) in game[target]) and ((col+2, row) in game[target]) and ((col+3, row) not in all_points) and ((col-1, row) in block_points):
            score += 5
            
        
        # noblock +
        #           target + 
        #                       target +
        #                                   target +
        #                                               opposite
        if ((col+1, row+1) in game[target]) and ((col+2, row+2) in game[target]) and ((col+3, row+3) in block_points) and ((col-1, row-1) not in all_points):
            score += 5
            
        # opposite +
        #           target + 
        #                       target +
        #                                   target +
        #                                               noblock
        elif((col+1, row+1) in game[target]) and ((col+2, row+2) in game[target]) and ((col+3, row+3) not in all_points) and ((col-1, row-1) in block_points):
            score += 5
            
            
        #                                           + noblock
        #                                 + target
        #                     + target 
        #         + target  
        # opposite 
        if((col+1, row-1) in game[target]) and ((col+2, row-2) in game[target]) and ((col+3, row-3) in block_points) and ((col-1, row+1) not in all_points):
            score += 5
            
        #                                           + opposite
        #                                 + target
        #                     + target 
        #         + target  
        # noblock 
        elif((col+1, row-1) in game[target]) and ((col+2, row-2) in game[target]) and ((col+3, row-3) not in all_points) and ((col-1, row+1) in block_points):
            score += 5  
            
                
    return score 


def three_stone_no_block(game, target, opposite): # 연속된 세 돌과 막은 돌 없음
    global outbounds
    all_points = game[target] + game[opposite] + outbounds
    block_points = game[opposite] + outbounds 
    score = 0 
    
    for (col, row) in game[target]:
        # noblock + target + target + target + noblock
        if ((col, row+1) in game[target]) and ((col, row+2) in game[target]) and ((col, row+3) not in all_points) and ((col, row-1) not in all_points):
            score += 20
            
            
        # noblock +
        # target + 
        # target + 
        # target + 
        # noblock 
        if ((col+1, row) in game[target]) and ((col+2, row) in game[target]) and ((col+3, row) not in all_points) and ((col-1, row) not in all_points):
            score += 20
            
            
        # noblock +
        #           target +
        #                       target +
        #                                   target +
        #                                               noblock
        if ((col+1, row+1) in game[target]) and ((col+2, row+2) in game[target]) and ((col+3, row+3) not in all_points) and ((col-1, row-1) not in all_points):
            score += 20
            
            
        #                                           + noblock
        #                                 + target
        #                     + target 
        #         + target 
        # noblock 
        if ((col+1, row-1) in game[target]) and ((col+2, row-2) in game[target]) and ((col+3, row-3) not in all_points) and ((col-1, row+1) not in all_points):
            score += 20
            
    
    return score 


def four_stone_two_block(game, target, opposite): # 연속된 네 돌과 두 돌이 막았을 때, 가능성을 올려주기 때문에 점수에 추산
    global outbounds
    all_points = game[target] + game[opposite] + outbounds
    block_points = outbounds + game[opposite]
    score = 0
    
    for (col, row) in game[target]:
        # opposite + target + target + target + target + opposite
        if ((col, row+1) in game[target]) and ((col, row+2) in game[target]) and ((col, row+3) in game[target]) and ((col, row-1) in block_points) and ((col, row+4) in block_points):
            score += 20
            
        
        # oppostie +    
        # target +
        # target +
        # target +
        # target + 
        # opposite
        if ((col+1, row) in game[target]) and ((col+2, row) in game[target]) and ((col+3, row) in game[target]) and ((col+4, row) in block_points) and ((col-1, row) in block_points):
            score += 20
            
        
        # opposite + 
        #           target +  
        #                     target +  
        #                                 target +  
        #                                             target + 
        #                                                       opposite
        if ((col+1, row+1) in game[target]) and ((col+2, row+2) in game[target]) and ((col+3, row+3) in game[target]) and ((col+4, row+4) in block_points) and ((col-1, row-1) in block_points):
            score += 20
            
        
        #                                                         opposite
        #                                             target + 
        #                                 target +  
        #                     target +  
        #           target +  
        # oppostie +
        if ((col+1, row-1) in game[target]) and ((col+2, row-2) in game[target]) and ((col+3, row-3) in game[target]) and ((col+4, row-4) in block_points) and ((col-1, row+1) in block_points):
            score += 20
            
        
    return score
    

def four_stone_one_block(game, target, opposite): # 연속된 네 돌과 한 돌이 막았을 때
    global outbounds
    all_points = game[target] + game[opposite] + outbounds
    block_points = outbounds + game[opposite]
    score = 0
    
    for (col, row) in game[target]:
        # noblock + target + target + target + target + opposite
        if ((col, row+1) in game[target]) and ((col, row+2) in game[target]) and ((col, row+3) in game[target]) and ((col, row-1) not in all_points) and ((col, row+4) in block_points):
            score += 50
            
        # opposite + target + target + target + target + noblock
        elif((col, row+1) in game[target]) and ((col, row+2) in game[target]) and ((col, row+3) in game[target]) and ((col, row-1) in block_points) and ((col, row+4) not in all_points):
            score += 50
            
        
        # noblock +    
        # target +
        # target +
        # target +
        # target + 
        # opposite
        if ((col+1, row) in game[target]) and ((col+2, row) in game[target]) and ((col+3, row) in game[target]) and ((col+4, row) in block_points) and ((col-1, row) not in all_points):
            score += 50
            
        # opposite + 
        # target +
        # target +
        # target +
        # target + 
        # noblock  
        elif ((col+1, row) in game[target]) and ((col+2, row) in game[target]) and ((col+3, row) in game[target]) and ((col+4, row) not in all_points) and ((col-1, row) in block_points):
            score += 50
            
        
        # noblock + 
        #           target +  
        #                     target +  
        #                                 target +  
        #                                             target + 
        #                                                       opposite
        if ((col+1, row+1) in game[target]) and ((col+2, row+2) in game[target]) and ((col+3, row+3) in game[target]) and ((col+4, row+4) in block_points) and ((col-1, row-1) not in all_points):
            score += 50 
            
        # opposite + 
        #           target +  
        #                     target +  
        #                                 target +  
        #                                             target + 
        #                                                       noblock 
        elif ((col+1, row+1) in game[target]) and ((col+2, row+2) in game[target]) and ((col+3, row+3) in game[target]) and ((col+4, row+4) not in all_points) and ((col-1, row-1) in block_points):
            score += 50
            
        
        #                                                         noblock
        #                                             target + 
        #                                 target +  
        #                     target +  
        #           target +  
        # oppostie +
        if ((col+1, row-1) in game[target]) and ((col+2, row-2) in game[target]) and ((col+3, row-3) in game[target]) and ((col+4, row-4) in block_points) and ((col-1, row+1) not in all_points):
            score += 50
            
        #                                                       oppostie
        #                                             target + 
        #                                 target +  
        #                     target +  
        #           target +  
        # noblock + 
        elif ((col+1, row-1) in game[target]) and ((col+2, row-2) in game[target]) and ((col+3, row-3) in game[target]) and ((col+4, row-4) not in all_points) and ((col-1, row+1) in block_points):
            score += 50
            
    
    return score


def four_stone_no_block(game, target, opposite): # 연속된 네 돌이 모여있고 막힌 돌이 없을 때
    global outbounds
    all_points = game[target] + game[opposite] + outbounds 
    block_points = outbounds + game[opposite]
    score = 0
    
    for (col, row) in game[target]:
        # noblock + target + target + target + target + noblock
        if ((col, row+1) in game[target]) and ((col, row+2) in game[target]) and ((col, row+3) in game[target]) and ((col, row+4) not in all_points) and ((col, row-1) not in all_points):
            score += 1000
            
         
        # noblock +   
        # target +
        # target +
        # target +
        # target + 
        # noblock
        if ((col+1, row) in game[target]) and ((col+2, row) in game[target]) and ((col+3, row) in game[target]) and ((col+4, row) not in all_points) and ((col-1, row) not in all_points):
            score += 1000
            
        
        # noblock +
        #           target +  
        #                     target +  
        #                                 target +  
        #                                             target +
        #                                                       noblock 
        if ((col+1, row+1) in game[target]) and ((col+2, row+2) in game[target]) and ((col+3, row+3) in game[target]) and ((col+4, row+4) not in all_points) and ((col-1, row-1) not in all_points):
            score += 1000
            
        
        #                                                         noblock 
        #                                             target +
        #                                 target +  
        #                     target +  
        #           target + 
        # noblock +
        if ((col+1, row-1) in game[target]) and ((col+2, row-2) in game[target]) and ((col+3, row-3) in game[target]) and ((col+4, row-4) not in all_points) and ((col-1, row+1) not in all_points):
            score += 1000
            
            
    return score


def five_stone(game, target, opposite): # 다섯 돌이 모여있을 때
    global outbounds
    all_points = game[target] + game[opposite]
    block_points = outbounds + game[opposite]
    score = 0
    
    for (col, row) in game[target]:
        # target + target + target + target + target
        if ((col, row+1) in game[target]) and ((col, row+2) in game[target]) and ((col, row+3) in game[target]) and ((col, row+4) in game[target]):
            score += 300000
            
        
        # target + 
        # target + 
        # target + 
        # target + 
        # target
        if ((col+1, row) in game[target]) and ((col+2, row) in game[target]) and ((col+3, row) in game[target]) and ((col+4, row) in game[target]):
            score += 300000
            
            
        # target + 
        #           target + 
        #                       target + 
        #                                   target + 
        #                                               target
        if ((col+1, row+1) in game[target]) and ((col+2, row+2) in game[target]) and ((col+3, row+3) in game[target]) and ((col+4, row+4) in game[target]):
            score += 300000
            
        
        #                                               target        
        #                                   target + 
        #                       target + 
        #           target + 
        # target + 
        if ((col-1, row+1) in game[target]) and ((col-2, row+2) in game[target]) and ((col-3, row+3) in game[target]) and ((col-4, row+4) in game[target]):
            score += 300000
            
            
    return score