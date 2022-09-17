import sys
input = sys.stdin.readline
import heapq

'''
최소 스패닝 트리!

정점 선택을 기반으로 하는 Prim MST 알고리즘으로 풀이했다.
'''

V, E = map(int, input().split())            # 정점 개수, 간선 개수
link = [[] for _ in range(V)]               # link[i] = i번 정점에서 갈 수 있는 (비용, 정점) 목록
for _ in range(E):
    A, B, C = map(int, input().split())
    link[A-1] += [(C, B-1)]
    link[B-1] += [(C, A-1)]

ans = 0
visited = [0] * V                       # 방문 배열
cost = [1000001] * V                    # cost[i] = i번 노드로 오는 간선 중 최소 비용
Q = [(0, 0)]                            # 0번 정점에서 비용 0으로 시작
while Q:
    c, now = heapq.heappop(Q)           # 연결된 정점 중에 비용이 최소인 정점으로 이동
    if visited[now]:                    # 이미 방문한 곳이라면 pass
        continue
    ans += c                            # 전체 비용에 추가
    visited[now] = 1                    # 방문 처리
    for c, nxt in link[now]:               # 현재 정점에서 연결된 정점 중에
        if not visited[nxt] and cost[nxt] > c:  # 지금까지의 최소 비용보다 더 낮은 비용으로 갈 수 있는 미방문 정점이 있으면
            heapq.heappush(Q, (c, nxt))             # enqueue
            cost[nxt] = c                           # 최소 비용 갱신
print(ans)
