import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


# 가능한 경로의 수를 세는 함수
def dfs(i, j):
    if (i, j) == (M-1, N-1):                # 도착점에 도착하면
        return 1                                # 도착점까지 가능한 경로 개수는 1개
    if dp[i][j] != -1:                      # 이미 방문했던 지점이면
        return dp[i][j]                         # 해당 지점에서 도착점까지 갈 수 있는 경로의 개수 반환

    dp[i][j] = 0                            # 방문 처리
    for d in range(4):                      # 상하좌우 중 이동 가능한 칸에 대해
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < M and 0 <= nj < N and Map[i][j] > Map[ni][nj]:
            dp[i][j] += dfs(ni, nj)             # 가능한 경로 수를 합산

    return dp[i][j]


M, N = map(int, input().split())            # 행 개수, 열 개수
Map = [list(map(int, input().split())) for _ in range(M)]
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]       # 상하좌우
dp = [[-1] * N for _ in range(M)]           # dp[i][j] = (i, j)에서 도착 지점까지 갈 수 있는 경로의 개수
print(dfs(0, 0))