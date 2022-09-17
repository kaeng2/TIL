import sys
input = sys.stdin.readline
import heapq


'''
최소 스패닝 트리!

Kruskal 알고리즘의 시간 복잡도 = O( 간선 수 * log2(간선 수) )
Prim 알고리즘의 시간 복잡도 = O( 정점 수 ** 2 )

정점 개수는 최대 1,000개이고 간선 개수는 최대 100,000개라서
정점 선택을 기반으로 하는 Prim MST 알고리즘으로 풀이했다.
'''

N, M = int(input()), int(input())           # 컴퓨터의 수, 선의 수
link = [[] for _ in range(N)]               # link[i] = i와 연결된 (비용, 정점)
visited = [0] * N                           # 방문 배열
cost = [10000] * N                          # cost[i] = i번 정점으로 들어오는 간선 중 (현재까지의) 최소 비용

for _ in range(M):
    a, b, c = map(int, input().split())
    link[a-1] += [(c, b-1)]
    link[b-1] += [(c, a-1)]

Q = [(0, 0)]                                    # 0번 정점에서 비용 0으로 시작
ans = 0
while Q:
    cst, now = heapq.heappop(Q)                 # 비용이 가장 낮은 정점으로 이동
    if visited[now]:                            # 이미 방문했다면 pass
        continue
    ans += cst                                  # 총 비용에 추가
    visited[now] = 1                            # 방문 처리
    for cst, nxt in link[now]:                  # 연결된 정점 중에
        if not visited[nxt] and cost[nxt] > cst:    # 미방문한 nxt로 들어가는 현재까지의 최소 비용보다 비용이 더 적은 간선이 나타나면
            heapq.heappush(Q, (cst, nxt))               # enqueue
            cost[nxt] = cst                             # 최소 비용 갱신
print(ans)