import sys
input = sys.stdin.readline

'''
n이 11 이하의 양수이므로 마지막 인덱스가 11인 dp 배열을 미리 만들어두었다.
dp[0] ~ dp[3]까지는 값을 미리 채워두었다.
4 이상의 i에 대해 i를 1, 2, 3의 합으로 나타내는 방법은 다음과 같다.
    1. i-1을 1, 2, 3의 합으로 나타낸 덧셈식에 1을 더해서 나타내는 방법
    2. i-2를 1, 2, 3의 합으로 나타낸 덧셈식에 2를 더해서 나타내는 방법
    3. i-3을 1, 2, 3의 합으로 나타낸 덧셈식에 3을 더해서 나타내는 방법
따라서 dp[i] = dp[i-1] + dp[i-2] + dp[i-3] 이 성립한다.
'''

T = int(input())
for t in range(T):
    n = int(input())
    dp = [0, 1, 2, 4] + [0] * 8
    if n > 3:
        for i in range(4, n+1):
            dp[i] += sum(dp[i-3:i])
    print(dp[n])