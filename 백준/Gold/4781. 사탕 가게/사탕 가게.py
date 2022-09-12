import sys
input = sys.stdin.readline

'''
Knapsack!
근데 동일한 사탕을 얼마든지 더 담을 수 있다는 점에서 평범한 배낭 문제와는 약간 차이가 있다. 
평범한 배낭 문제 에서는 이차원 배열의 경우
    dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w] 였는데, 
이 문제에서는 이차원 배열의 경우
    dp[i][j] = max(dp[i-1][j], v + dp[i][j-w] 가 된다.
i번째 물건을 담고 남은 무게(가격)에서 더 담을 걸 고려할 때 i번째 물건을 또 고려해주는 것이다.

1차원 배열 dp의 경우
평범한 배낭 문제에서는 i가 M부터 해당 물건의 무게까지 거꾸로 돌면서 dp를 채웠다면,
이 문제에서는 i가 해당 물건의 가격(무게)에서부터 M까지 돌면서 dp를 채운다.
그래야 dp[i-p] 값이 i번째 물건까지 고려한 상태로 업데이트 되어 있기 때문이다.
'''

while True:
    N, M = map(float, input().split())
    N, M = int(N), int(M * 100 + 0.5)
    
    if not N:
        break
    
    dp = [0] * (M+1)
    for _ in range(N):
        c, p = map(float, input().split())
        c, p = int(c), int(p * 100 + 0.5)
    
        for i in range(p, M+1):
            dp[i] = max(dp[i], c + dp[i-p])
    
    print(dp[M])