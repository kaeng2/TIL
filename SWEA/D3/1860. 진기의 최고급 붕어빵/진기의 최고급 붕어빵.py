# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # 입력
    N, M, K = map(int, input().split())
    cstmr = list(map(int, input().split()))
    # 재고
    storage = 0
    # 마지막 손님이 오는 시간까지
    for i in range(max(cstmr)+1):
        # 0초를 제외하고 M초마다 재고에 K개가 추가됨
        if i % M == 0 and i != 0:
            storage += K
        # 손님이 올 때마다 재고가 한 개씩 줄어듦
        if i in cstmr:
            storage -= 1
        # 재고가 음수가 되는 순간 반복문 종료
        if storage < 0:
            result = 'Impossible'
            break
    # 재고가 한 번도 음수가 되지 않고 마지막 손님까지 끝난 경우
    else:
        result = 'Possible'
    # 출력
    print(f'#{t} {result}')