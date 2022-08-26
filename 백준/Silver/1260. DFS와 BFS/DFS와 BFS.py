import sys
input = sys.stdin.readline
from collections import deque


def dfs(v):
    global dfs_history
    now = v
    for nxt in link[now]:
        if not dfs_visited[nxt]:
            dfs_visited[nxt] = 1
            dfs_history.append(nxt)
            dfs(nxt)
    return


def bfs():
    Q = deque([V])
    while Q:
        now = Q.popleft()
        for nxt in link[now]:
            if not bfs_visited[nxt]:
                Q.append(nxt)
                bfs_history.append(nxt)
                bfs_visited[nxt] = 1
    return


N, M, V = map(int, input().split())     # 정점 개수, 간선 개수, 시작점
link = [[] for _ in range(N+1)]
for _ in range(M):                      # 연결 정보 기록
    x, y = map(int, input().split())
    link[x] += [y]
    link[y] += [x]
for node in link:                       # 번호가 작은 순서대로 정렬
    node.sort()

# DFS
dfs_history = deque([V])    # 방문 순서
dfs_visited = [0] * (N+1)   # 방문 체크
dfs_visited[V] = 1          # 출발점 설정
dfs(V)
print(*dfs_history)
# BFS
bfs_history = deque([V])    # 방문 순서
bfs_visited = [0] * (N+1)   # 방문 체크
bfs_visited[V] = 1          # 출발점 설정
bfs()
print(*bfs_history)