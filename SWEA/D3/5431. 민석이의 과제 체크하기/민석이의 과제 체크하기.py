test = int(input())
for t in range(1, test+1):
    N, K = map(int, input().split())
    print(f'#{t}', end=' ')
    numbers = list(map(int, input().split()))
    for i in list(range(1, N+1)):
        if i not in numbers:
            print(i, end=' ')
    print()