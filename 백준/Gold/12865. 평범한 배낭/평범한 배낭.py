import sys
input = sys.stdin.readline

'''
유명한 0-1 Knapsack 문제라고 한다.

(N+1) * (K+1) 사이즈의 DP 배열을 만든다.
dp[i][j] 값은 가방 무게 제한이 j kg일때 처음 i개의 물건 중 담을 수 있는 최대 가치를 의미한다.

만약 j번째 물건의 무게가 j kg을 넘어간다면 i번째 물건은 담을 수 없으므로, 
같은 무게에서 처음 i-1개의 물건 중 담을 수 있는 최대 가치인 dp[i-1][j]가 최대값이 된다.

만약 j번째 물건의 무게가 j kg을 넘지 않아서 j번째 물건을 담을지 말지 선택할 수 있다면,
    1. 담지 않는 경우 -> dp[i-1][j]
    2. 담는 경우 -> dp[i-1][j번째 물건을 담고 나서 추가적으로 더 채울 수 있는 무게]
위의 두 경우 중 더 큰 값이 dp[i][j] 값이 된다.

최종 정답은 무게 제한이 K일 때 처음 N개의 물건 중 담을 수 있는 최대 가치, 즉 dp[N][K]가 된다. 
'''

N, K = map(int, input().split())
things = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]
for j in range(1, K+1):
    for i in range(1, N+1):
        if things[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-things[i][0]] + things[i][1], dp[i-1][j])
print(dp[N][K])