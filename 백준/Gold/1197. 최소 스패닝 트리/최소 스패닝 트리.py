import sys
input = sys.stdin.readline
import heapq


'''
최소 스패닝 트리!

정점 개수는 최대 10,000개이고 간선 개수는 최대 100,000개라서
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
Q = [(0, 0)]                            # 0번 정점에서 비용 0으로 시작
while Q:
    cost, now = heapq.heappop(Q)        # 연결된 정점 중에 비용이 최소인 정점으로 이동
    if visited[now]:                    # 이미 방문한 곳이라면 pass
        continue
    ans += cost                         # 전체 비용에 추가
    visited[now] = 1                    # 방문 처리
    for nxt in link[now]:               # 현재 정점에서 연결된 정점 전부 enqueue
        heapq.heappush(Q, nxt)
print(ans)