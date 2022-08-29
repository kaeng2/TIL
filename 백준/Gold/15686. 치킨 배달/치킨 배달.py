import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())                                # 마을 크기, 최대 치킨집 개수
town = [list(map(int, input().split())) for _ in range(N)]      # 마을 정보
chicken, house = [], []
for i in range(N):                                              # 마을 전체를 순회하면서
    for j in range(N):
        if town[i][j] == 2:                                         # 치킨집 좌표 리스트와
            chicken += [[i, j]]
        elif town[i][j] == 1:                                       # 집 좌표 리스트를 만들어준다
            house += [[i, j]]
result = []
for m in range(M, 0, -1):                                       # 치킨집 개수를 M개에서 1개까지 줄여가면서
    for c in combinations(chicken, m):                              # 가능한 조합을 만들고
        chicken_dist = 0
        for i, j in house:                                              # 각각의 집의
            mn = 100
            for x, y in c:
                mn = min(mn, abs(x-i) + abs(y-j))                   
            chicken_dist += mn                                              # 치킨 거리를 구해서 모두 합해준다
        result += [chicken_dist]                                        # 그 결과가 해당 조합의 총 치킨거리!
print(min(result))                                              # 모든 조합의 총 치킨 거리 중 최소값 출력