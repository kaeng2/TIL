import sys
input = sys.stdin.readline

'''
dp 배열은 다음과 같이 채워진다.

dp[i][0] = i번째 집을 빨간색으로 칠했을 경우 0번째 집부터 i번째 집까지를 칠하는 최소 비용
dp[i][1] = i번째 집을 초록색으로 칠했을 경우 0번째 집부터 i번째 집까지를 칠하는 최소 비용
dp[i][2] = i번째 집을 파란색으로 칠했을 경우 0번째 집부터 i번째 집까지를 칠하는 최소 비용

i-1번째 집은 i번째 집과 같은 색으로 칠할 수 없으므로, 
i번째 집에 칠한 색을 제외한 다른 색으로 칠하는 경우 중에서 최소 비용 + i번째 집을 칠하는 비용이 dp[i]의 원소가 된다.
'''

# 입력
N = int(input())                                                # 집의 개수
cost = [list(map(int, input().split())) for _ in range(N)]      # cost[i] = i번째 집을 RGB로 칠하는 비용
# dp 채우기
dp = [[0] * 3 for _ in range(N)]                                
dp[0] = cost[0]
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
# 출력
print(min(dp[N-1]))