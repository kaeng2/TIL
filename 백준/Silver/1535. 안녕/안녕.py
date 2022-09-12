import sys
input = sys.stdin.readline

'''
Knapsack!
'''

N = int(input())
damage = list(map(int, input().split()))
joy = list(map(int, input().split()))
dp = [0] * 100
for i in range(N):
    for j in range(99, damage[i]-1, -1):
        dp[j] = max(dp[j], joy[i] + dp[j-damage[i]])
print(dp[99])