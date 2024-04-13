import evaluate as ev

def make_computer_choice(game, color): # game 의 상태에서 computer가 다음 선택을 출력
    tmp_game = {"b": game["b"].copy(), "w": game["w"].copy()}
    if ( color == "b") and (len(game["w"]) == 0):
        search_position = (9, 9) # 첫 시작을 항상 가운데에서 시작
    else:
        depth = 3
        candidate_points = make_candidate_board(game, depth)
        heuristic_score, search_position = alpha_beta_search(tmp_game, candidate_points, depth, color, float("-inf"), float("inf"))
    return search_position


def alpha_beta_search(game, candidate_points, depth, color, alpha, beta, maximizing_computer=True):
    all_points = game["b"] + game["w"]
    if ( color == "b"): # 컴퓨터가 b 일때
        player = "w"
    else:
        player = "b"

    if (depth == 0):
        return ev.evaluate(game, color), (0, 0)

    if (maximizing_computer): # computer가 둘 차례에서의 최댓값 찾기
        max_eval = float("-inf")
        max_point=(0, 0)

        for point in candidate_points:
            if(point in all_points): # 이미 있는 점 중복 탐색 방지
                continue
            
            game[color].append(point)

            eval, _ = alpha_beta_search(game, candidate_points, depth-1, color, alpha, beta, False)

            game[color].remove(point)
            
            if (eval > max_eval):
                max_eval = eval
                max_point = point
                alpha = max(alpha, max_eval)
                

            if (beta <= max_eval): # 가지치기
                break
                   
        return max_eval, max_point

    else: # player 가 둘 차례에서의 최솟값 찾기
        min_eval = float("inf")
        min_point = (0, 0)
        for point in candidate_points:
            if(point in all_points): # 이미 있는 점 중복 탐색 방지
                continue
            
            game[player].append(point)
            
            eval, _ = alpha_beta_search(game, candidate_points, depth-1, color, alpha, beta)
            
            game[player].remove(point)

            if (eval < min_eval):
                min_eval = eval
                min_point = point
                beta = min(beta, min_eval)

            if (min_eval <= alpha):    
                break
            
        return min_eval, min_point
    

def make_candidate_board(game, depth): # 모든 보드를 탐색하는 것이 아니라 오목이 일어나는 곳의 경계로부터 1칸 이내로 설정
    points = game["b"] + game["w"] 
    left_end = min(point[1] for point in points)
    right_end = max(point[1] for point in points)
    top_end = min(point[0] for point in points)
    bottom_end = max(point[0] for point in points)

    
    limit = min((depth+1)//2, len(points))
    
    left_limit = max(1, left_end - limit)
    right_limit = min(19, right_end + limit)
    top_limit = max(1, top_end - limit)
    bottom_limit = min(19, bottom_end + limit)

    candidate_points = []

    for i in range(top_limit, bottom_limit + 1):
        for j in range(left_limit, right_limit + 1):
            candidate_points.append((i, j))

    return candidate_points



    
    

