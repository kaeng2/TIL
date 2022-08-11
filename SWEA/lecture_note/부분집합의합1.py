# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # 집합
    st = list(map(int, input().split()))
    # 집합의 원소 개수
    n = len(st)
    
    # 각 부분집합에 대해서
    for i in range(1, 1<<n):
        sm = 0
        # j번째 원소가 들어있다면 해당 원소를 sm에 더해줌
        for j in range(n):
            if i & (1 << j):
                sm += st[j]
        # i번째 부분집합의 원소를 다 더한 값이 0이면 1을 출력
        if sm == 0:
            print(f'#{t} 1')
            break
    # 원소의 합이 0인 경우가 없었다면 0 출력
    else:
        print(f'#{t} 0') 