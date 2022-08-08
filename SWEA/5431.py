test = int(input())
for t in range(1, test+1):
    N, K = map(int, input().split())
    print(f'#{t}', end=' ')
    numbers = list(map(int, input().split()))
    
    # [1, 2, 3, ..., N]을 순회하면서
    for i in list(range(1, N+1)):
        # i가 제출 번호에 없으면 출력한다
        if i not in numbers:
            print(i, end=' ')
    # 다하면 줄바꿈
    print()