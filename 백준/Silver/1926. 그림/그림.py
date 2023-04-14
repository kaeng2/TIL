import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 입력
n, m = map(int, input().split())    # 세로, 가로 크기
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
def get_painting_size(i, j):
    global size
    
    if paper[i][j] == 0:
        return
    
    visited[i][j] = 1
    size += 1
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < n and 0 <= nj < m and paper[ni][nj] and not visited[ni][nj]:
            # visited[ni][nj] = 1
            # size += 1
            get_painting_size(ni, nj)
    return

largest, cnt = 0, 0
for x in range(n):
    for y in range(m):
        if paper[x][y] and not visited[x][y]:
            size = 0
            get_painting_size(x, y)
            largest = max(largest, size)
            cnt += 1
print(cnt)
print(largest)