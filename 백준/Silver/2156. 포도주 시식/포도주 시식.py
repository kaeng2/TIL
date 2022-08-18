# 포도주 잔의 개수
n = int(input())
# 포도주의 양 리스트
wine = [0] + [int(input()) for _ in range(n)]

if n < 3:
    print(sum(wine))
else:
    # i번째 잔까지 왔을 때 마실 수 있는 포도주의 최대량을 기록
    memo = [0] * (n+1)
    # 초기값 설정
    memo[1], memo[2] = wine[1], wine[1]+wine[2]
    # 점화식 이용하여 memo 리스트 채우기
    for i in range(3, n+1):
        # i번째 잔을 안 마시는 경우 최대량은 memo[i-1]
        # i번째 잔을 마시는 경우
            # i-2번째 잔까지의 최대값 memo[i-2] + i번째 포도주 wine[i]
            # i-3번째 잔까지의 최대값 memo[i-3] + i-1번째 포도주 wine[i-1] + i번째 포도주 wine[i]
        # 위 세 케이스 중의 최대값이 i번째 잔까지의 최대값!
        memo[i] = max(memo[i-1], memo[i-2] + wine[i], memo[i-3] + wine[i-1] + wine[i])
    # 출력
    print(memo[n])