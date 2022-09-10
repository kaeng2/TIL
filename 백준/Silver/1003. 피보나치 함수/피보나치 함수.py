import sys
input = sys.stdin.readline

T = int(input())                           # 테스트 케이스 개수
tc = [int(input()) for _ in range(T)]      # 각 테스트 케이스의 N 기록
n = max(tc, default=-1)
dp = [[1, 0]] + [[0, 0] for _ in range(n)]   # 테스트 케이스의 최대값만큼 dp 배열을 만든다
'''
dp[i] = fibo(i)를 호출했을 때 출력되는 [ 0의 개수, 1의 개수 ]
'''
if n >= 1:
    dp[1] = [0, 1]
    for i in range(2, n+1):
        dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]
for N in tc:
    print(*dp[N])       # 테스트 케이스마다 dp 배열 값 출력