from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    memory = defaultdict(int)
    for person, score in zip(name, yearning):
        memory[person] = score
        print(memory)
    for p in photo:
        m = 0
        print(p)
        for person in p:
            m += memory[person]
        answer += [m]
    
    return answer