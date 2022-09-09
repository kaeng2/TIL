import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque

N, M = map(int, input().split())                        # 정점의 개수, 간선의 개수
link = [[] for _ in range(N)]                           # 연결 리스트
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())     # 인덱스로 활용할 수 있도록 1을 빼줬다
    link[u] += [v]
    link[v] += [u]
visited = [0] * N                                       # 방문 배열
ans = 0                                                 # 연결 요소 개수
# bfs 실행
for i in range(N):                      # 정점을 돌면서
    if not visited[i]:                      # 아직 미방문 했다면
        Q = deque([i])                          # 해당 정점을 시작으로 bfs 실행
        visited[i] = 1
        while Q:                                    
            now = Q.popleft()
            for nxt in link[now]:                   # 해당 정점과 연결된 모든 정점을 순회하면서
                if not visited[nxt]:                    # 방문 처리 및 enqueue
                    visited[nxt] = 1
                    Q.append(nxt)
        ans += 1                                # 연결 요소를 하나 찾을 때마다 ans에 +1
print(ans)