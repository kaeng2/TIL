from itertools import combinations
from collections import defaultdict
def solution(weights):
    mate = defaultdict(int)
    answer = 0
    weights.sort(reverse=True)
    for weight in weights:
        answer += mate[6 * weight] + mate[8 * weight] + mate[9 * weight] + mate[12 * weight]
        mate[6 * weight] += 1
    
    return answer