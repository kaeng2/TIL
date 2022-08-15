# 테스트 케이스 개수
test = int(input())
# 돈의 종류
cash = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# 각 테스트 케이스마다
for t in range(1, test+1):
    # 거슬러 주어야 할 금액
    N = int(input())
    # 테스트 케이스 번호부터 출력하고, 
    print(f'#{t}')
    # 금액이 높은 돈부터 낼 수 있는만큼 내고 남은 금액을 다시 N에 저장한 후, 
    # 몇 개나 냈는지 출력
    # 그 다음으로 금액이 높은 돈으로 또 반복
    for c in cash:
        count = N // c
        N %= c
        # end에 공백을 주어 결과가 한 줄에 출력될 수 있도록 함
        print(count, end=' ')
    # 전부 출력하면 줄바꿈
    print()