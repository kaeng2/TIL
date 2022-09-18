import sys
input = sys.stdin.readline
import heapq
import math

'''
최소 스패닝 트리!

Kruskal 알고리즘의 시간 복잡도 = O( 간선 수 * log2(간선 수) )
Prim 알고리즘의 시간 복잡도 = O( 정점 수 ** 2 )

정점 개수는 최대 100개이고 간선 개수는 최대 (100 choose 2) = 4950개라서
정점 선택을 기반으로 하는 Prim MST 알고리즘으로 풀이했다.

보통의 Prim MST 알고리즘과 동일하나, 주어진 좌표를 활용해 간선의 가중치를 직접 구해주어야 했다.
'''


# 기준이 될 별의 인덱스를 받아서 해당 별에서 다른 모든 별까지의 거리를 리스트 형태로 반환하는 함수
def get_dist_from(here):
    return [math.sqrt((loca[i][0] - loca[here][0])**2 + (loca[i][1] - loca[here][1])**2) for i in range(N)]


# 입력
N = int(input())                        # 별의 개수
loca = []                               # loca[i] = i번째 별의 (x좌표, y좌표)
for _ in range(N):
    x, y = map(float, input().split())
    loca.append((x, y))

# 탐색 준비
visited = [0] * N                       # 방문 배열
dist = [float("inf")] * N               # dist[i] = i번째 별로 들어오는 선의 최소 길이
ans = 0                                 # 별자리의 총 길이
Q = [(0, 0)]                            # 0번째 별부터 출발
heapq.heapify(Q)

# 탐색
while Q:
    c, i = heapq.heappop(Q)             # 현재 별로 들어오는 선의 길이, 현재 별의 인덱스

    if visited[i]:                      # 이미 이어진 별이면 pass
        continue
    visited[i] = 1                      # 방문 처리
    ans += c                            # 별자리 길이 갱신
    d = get_dist_from(i)                # d[j] = i번째 별에서부터 j번째 별까지의 거리

    for j in range(N):                          # j번 별이
        if not visited[j] and dist[j] > d[j]:       # 미방문 했고, 현재까지 알려진 최소 거리보다 더 가까운 곳에 있으면
            heapq.heappush(Q, (d[j], j))                # (i~j번째 별 사이 거리, j) enqueue
            dist[j] = d[j]                              # 최소 거리 갱신

# 출력
print(f'{ans:.2f}')                     # 소수점 둘째 자리까지 출력