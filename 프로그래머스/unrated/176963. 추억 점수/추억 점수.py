from collections import defaultdict

def solution(name, score, photo):
    answer = []
    memory = defaultdict(int)
    for n, s in zip(name, score):
        memory[n] = s
    for p in photo:
        m = 0
        for person in p:
            m += memory[person]
        answer += [m]
    
    return answer