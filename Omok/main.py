# Omok Heuristic alpha-beta search

import end_test as et
import computer_choice as cc
import const
import print as p

def game_init(): # game 초기화
    b_points = []
    w_points = []
    game = {"b": b_points, "w": w_points}
    return game


if __name__ == "__main__":
    player = input("Choose your place : b(black) / w(white) \n")
    
    columns = const.COLUMNS
    rows = const.ROWS

    if ( player == "b" ): # player 가 선공
        computer = "w"
        game = game_init()
        p.draw("init")
        
        while(True):
            player_choice = input("검은돌을 놓을 자리를 선택하세요 ex) 4,a : ")

            tmp = player_choice.strip().split(",")
            player_position = (columns[tmp[0]], rows[tmp[1]])

            if(player_position in game["b"] or player_position in game["w"]):
                print("이미 두어진 장소입니다. 다시 선택해 주세요.")
                continue
            
            p.draw(player_position)

            game["b"].append(player_position)

            pre_game = {"b": game["b"].copy(), "w": game["w"].copy()}
            
            state, color = et.state_func(game)
            if (state == "end"):
                print(state)
                break

            computer_position = cc.make_computer_choice(game, computer)
            game["w"].append(computer_position)

            post_game = {"b": game["b"].copy(), "w": game["w"].copy()}
            
            computer_giveup = et.is_computer_giveup(pre_game, post_game)

            if ( computer_giveup ):
                print("computer 가 포기하였습니다.")
                color = player
                break
            
            p.draw(computer_position)
            
            state, color = et.state_func(game)
            if (state == "end"):
                print(state)
                break

    elif(player == "w"): # player 가 후공
        computer = "b"
        game = game_init()

        computer_position = cc.make_computer_choice(game, computer)
        game["b"].append(computer_position)
        
        p.draw(computer_position)

        while(True):
            player_choice = input("흰돌을 놓을 자리를 선택하세요 ex)4,a : ")
            
            tmp = player_choice.strip().split(",")

            player_position = (columns[tmp[0]], rows[tmp[1]])

            if(player_position in game["b"] or player_position in game["w"]):
                print(game)
                print("이미 두어진 장소입니다.")
                continue

            p.draw(player_position)
            
            game["w"].append(player_position)

            pre_game = {"b": game["b"].copy(), "w": game["w"].copy()}
            
            state, color = et.state_func(game)
            if(state == "end"):
                print(state)
                break
            
            computer_position = cc.make_computer_choice(game, computer)
            game["b"].append(computer_position)

            post_game = {"b": game["b"].copy(), "w": game["w"].copy()}
            
            computer_giveup = et.is_computer_giveup(pre_game, post_game)
            
            if ( computer_giveup ):
                print("computer 가 포기하였습니다.")
                color = player
                break
            
            p.draw(computer_position)
            
            state, color = et.state_func(game)
            if(state == "end"):
                print(state)
                break

    else:
        player = None

    if not player: # 오타
        print("다시 시작해 주세요")
    elif (player == color): # player 승리 부분
        print("player가 승리하였습니다.")
    else: # computer 승리 부분
        print("computer가 승리하였습니다.")
        
        
