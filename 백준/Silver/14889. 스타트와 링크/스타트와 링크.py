import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())    # 사람 수     
S = [list(map(int, input().split())) for _ in range(N)]     # 능력치
mn = 1000
for start in combinations(range(N), N//2):              # 가능한 start 팀 조합마다
    link = [x for x in range(N) if x not in start]          # link 팀 조합을 만들고
    capa_s, capa_l = 0, 0
    for i in start:                                         # start 팀의 능력치 계산
        for j in start:
            capa_s += S[i][j]
    for i in link:                                          # link 팀의 능력치 계산
        for j in link:
            capa_l += S[i][j]
    mn = min(mn, abs(capa_s - capa_l))                      # 최소값이면 mn 갱신
print(mn)