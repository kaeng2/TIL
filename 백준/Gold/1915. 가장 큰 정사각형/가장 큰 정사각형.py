import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]

# dp[i][j] = arr[i][j]를 우측 하단 꼭짓점으로 하는 정사각형 중 가장 큰 정사각형의 한 변 길이
dp = [[0] * M for _ in range(N)]

ans = 0
for n in range(N):
    for m in range(M):
        # 첫 행과 첫 열
        if n == 0 or m == 0:
            dp[n][m] = arr[n][m]
        
        elif arr[n][m] == 1:
            dp[n][m] = min(dp[n-1][m-1], dp[n-1][m], dp[n][m-1]) + 1
        
        ans = max(ans, dp[n][m])    # 정답 갱신

# 너비 출력
print(ans**2)