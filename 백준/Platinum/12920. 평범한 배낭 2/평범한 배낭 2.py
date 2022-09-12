import sys
input = sys.stdin.readline

'''
평범한 배낭 문제와 동일하나 동일한 물건이 여러 개 존재할 수 있다.
단순히 동일한 물건의 개수만큼 동일한 w와 v에 대해 dp 배열을 추가로 갱신 해주었더니 시간초과가 났다.
게시판을 훑어보다가 엄청난 풀이!를 발견해서 따라 풀어보았다.

물건이 k개 있을 경우, 이걸 2**0개짜리, 2**1개짜리, 2**2개짜리, 2**3개짜리, ..., 의 묶음 상품으로 만든다.
각 묶음 상품은 1개씩만 존재한다.
이 물건을 1개 구매하려면 1개짜리를, 2개 구매하려면 2개짜리를, 3개 구매하려면 1개짜리 + 2개짜리를, 4개 구매하려면 4개짜리를 구매하면 된다.
k를 이진수로 변환했을 때의 모든 자릿수만큼 묶음 상품을 만들면 1개부터 k개까지 구매 가능한 모든 경우의 수를 표현할 수 있다.

예를 들어 k = 17 이라면 이진수로 변환했을 때 '10001'이고, 각 자릿수는 2**4, 2**3, 2**2, 2**1, 2**0이다. 
즉 1개짜리, 2개짜리, 4개짜리, 8개짜리, 16개짜리 묶음 상품을 한 개씩 만들면 1개 ~ 17개까지 구매하는 모든 경우를 표현할 수 있는 것이다.

그러나! 이 경우 모든 묶음 상품을 구매하게 되면 31개를 구매하는 셈이 된다. 
즉 1개 ~ 17개까지가 아니라 1개 ~ 31개까지 구매하는 모든 경우의 수가 되는 것이다.
따라서 묶음 상품을 만들고 나면 상품이 몇 개나 남아있는지를 체크하면서 
더 이상 2의 제곱수 개의 묶음 상품을 만들 수 없는 상황이 되면 남아 있는 상품 개수만큼만 묶음 상품을 만든다.
이러한 방식으로 k = 17일 때는 1개, 2개, 4개, 8개, 15개 짜리 묶음 상품을 만든다.

각 묶음 상품은 1개씩만 존재하므로 이후에는 일반적인 배낭 문제처럼 풀 수 있다.
'''

N, M = map(int, input().split())
dp = [0] * (M+1)
obj = []

# 묶음 상품 만들기
for _ in range(N):
    w, v, k = map(int, input().split())

    i = 1
    while k > 0:                            # 상품이 남아 있는 동안 반복
        bundle = min(k, i)                      # 몇 개짜리 묶음 상품을 만들건지 결정
        obj.append((w * bundle, v * bundle))    # obj에 묶음 상품 추가
        k -= i                                  # 남은 상품 개수 갱신
        i *= 2                                  # 묶음 상품 크기 늘리기

# dp 배열 채우기
for w, v in obj:
    for i in range(M, w-1, -1):
        dp[i] = max(dp[i], v + dp[i - w])

# 출력
print(dp[M])