# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # N일 동안의 매매가를 알고 있다
    N = int(input())
    # N일 동안의 매매가
    price = list(map(int, input().split()))

    income = 0
    while price:
        # 최대값 중 가장 오른쪽에 있는 값이 판매한 날의 index
        # price를 내림차순 정렬한 리스트에서 최대값의 index를 찾고,
        # 그 index를 원본 price 리스트에서의 index로 변환하여 sell에 저장한다
        sell = len(price)-1 - list(reversed(price)).index(max(price))
        # 판매하는 날의 가격 * 판매하는 날 이전까지의 원소 개수(매일 한 개씩 매수) - 판매하는 날 이전까지의 가격의 합
        income += price[sell]*sell - sum(price[:sell])
        # price 리스트에서 처음부터 판매한 날까지의 정보를 삭제한다
        price = price[sell+1:]
        # price 리스트가 빌 때까지 반복
    print(f'#{t} {income}')