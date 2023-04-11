def solution(players, callings):
    name_dict = {}
    rank_dict = {}
    
    for i in range(len(players)):
        name_dict[players[i]] = i
        rank_dict[i] = players[i]

    for cur_player in callings:
        cur_rank = name_dict[cur_player]
        pre_player = rank_dict[cur_rank-1]
        name_dict[pre_player] = cur_rank
        name_dict[cur_player] = cur_rank - 1
        rank_dict[cur_rank] = pre_player
        rank_dict[cur_rank-1] = cur_player
    
    answer = []
    for i in range(len(players)):
        answer += [rank_dict[i]]
        
    return answer 