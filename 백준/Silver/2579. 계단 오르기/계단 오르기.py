import sys
sys.stdin.readline

'''
dp[i] = i번째 계단까지 올랐을 때, i번째 계단을 밟는 경우의 최대값
i번째 계단을 밟는 경우는 다음과 같이 나뉜다
    1. i-1번째 계단을 안 밟고 i-2번째 계단을 밟는 경우                       -> dp[i-2]
    2. i-1번째 계단을 밟고 i-2번째 계단을 안 밟고 i-3번째 계단을 밟는 경우      -> scores[i-1] + dp[i-3]
따라서 dp[i]는 위의 두 가지 경우 중 최대값에 scores[i]를 더한 값이 된다.
'''

N = int(input())                                # 계단의 개수
scores = [int(input()) for _ in range(N)]       # 각 계단의 점수
# 계단이 3개 이상인 경우
if N > 2:
    dp = [0] * N
    dp[0:3] = [scores[0], scores[0] + scores[1], max(scores[0], scores[1]) + scores[2]]
    for i in range(3, N):
        dp[i] = max(dp[i-2], dp[i-3] + scores[i-1]) + scores[i]
    print(dp[N-1])
# 계단이 3개 미만인 경우
else:
    print(sum(scores))