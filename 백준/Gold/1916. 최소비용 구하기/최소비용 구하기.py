import sys
input = sys.stdin.readline
import heapq


def dijkstra(s, e):
    Q = []
    heapq.heappush(Q, (0, s))           # 출발점 ~> 출발점 비용은 0으로 설정
    cost = [100000 * N] * (N+1)
    cost[s] = 0
    while Q:                            # Q가 빌 때까지
        d, x = heapq.heappop(Q)             # Q에서 (출발점에서부터 해당 노드까지의 비용, 탐색할 노드) 를 꺼낸다 (비용이 가장 작은 걸로)
        if cost[x] < d:                     # 꺼낸 비용이 x까지 오는 최소 비용보다 크다면 넘어간다
            continue
        for y, c in link[x]:                # (x와 연결된 지점 y, x에서 y로 이동하는 비용 c)
            if d + c < cost[y]:                 # 출발점에서 x를 거쳐 y로 가는 비용이 출발점에서 y까지 가는 최소 비용보다 작다면
                cost[y] = d + c                     # 출발점에서 y까지 가는 최소 비용을 갱신한다
                heapq.heappush(Q, (cost[y], y))     # enqueue
    return cost[e]                      # 출발점에서 도착점까지의 최소 비용 반환


N = int(input())                                # 도시의 개수
M = int(input())                                # 버스의 개수
link = [[] for _ in range(N+1)]                 # link[i] = (i번 도시에서 갈 수 있는 도시, 그 비용)
for _ in range(M):                              # 노선, 비용 정보 입력
    x, y, c = map(int, input().split())
    link[x] += [(y, c)]
s, e = map(int, input().split())                # 출발 도시, 도착 도시
print(dijkstra(s, e))