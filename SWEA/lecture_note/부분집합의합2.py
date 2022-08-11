# 테스트 케이스 개수
test = int(input())
# 각 테스트케이스마다
for t in range(1, test+1):
    # 입력 받기
    N, K = map(int, input().split())
    # 조건을 만족하는 부분집합의 개수
    cnt = 0
    # 모든 부분집합에 대해
    for i in range(2**12):
        # 부분집합의 합
        sm = 0
        # 부분집합의 원소 개수
        elem = 0
        # 각각의 원소가 포함되는지 확인
        for j in range(12):
            # 해당 원소가 포함되면
            # 원소 개수를 하나 늘리고 해당 원소를 합에 더해준다
            if i & (1<<j):
                elem += 1
                sm += j+1
        # 한 부분집합에 대해 원소 개수와 원소의 합이 다 구해지면
        # 주어진 조건을 만족하는지 확인하고, 만족하면 cnt를 1 올린다
        if elem == N and sm == K:
            cnt += 1
    print(f'#{t} {cnt}')

