import sys
input = sys.stdin.readline
from collections import deque

def bfs_trash_size(sx, sy):
    Q = deque([(sx, sy)])
    visited[sx][sy] = 2
    size = 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 1:
                Q.append((nx, ny))
                visited[nx][ny] = 2
                size += 1
    return size


N, M, K = map(int, input().split())
visited = [[0] * M for _ in range(N)]
trash = []
for _ in range(K):
    r, c = map(lambda x: int(x)-1, input().split())
    visited[r][c] = 1
    trash += [(r, c)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = 0
for (tx, ty) in trash:
    if visited[tx][ty] == 1:
        size = bfs_trash_size(tx, ty)
        ans = max(ans, size)
print(ans)