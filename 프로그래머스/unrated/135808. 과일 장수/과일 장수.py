def solution(k, m, score):
    score.sort(reverse=True)
    box_num = len(score) // m

    answer = 0
    for i in range(box_num):
        answer += score[(i+1) * m - 1] * m
    return answer