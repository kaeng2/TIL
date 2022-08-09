## sum, min, max 함수 안 쓰고 풀기

# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # N, M과 정수 입력 받기
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    # 최대, 최소를 판단할 최초 기준값
    mn, mx = 1000000, 0
    # 리스트의 첫 원소부터
    for i in range(N-M+1):
        # M개 원소를 slicing하고,
        lst = num[i:i+M]
        summ = 0
        # lst의 합을 구한다
        for j in lst:
            summ += j
        # lst의 합이 기존의 최소값보다 작거나 기존의 최대값보다 크면 최대,최소값을 갱신한다
        if mn > summ:
            mn = summ
        if mx < summ:
            mx = summ
    print(f'#{t} {mx-mn}')
    
#####################################

# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # N, M과 정수 입력 받기
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    # 가장 처음부터 M개 칸의 합
    sm = 0
    for n in num[:M]:
        sm += n
    # 최대, 최소 기준값
    mx, mn = sm, sm
    # 최초 합에서 추가되는 원소는 더해주고 버려지는 원소는 빼준다
    # 최대값 최소값 갱신
    for i in range(M, N):
        sm += num[i] - num[i-M]
        if mx < sm:
            mx = sm
        if mn > sm:
            mn = sm
    print(f'#{t} {mx-mn}')
