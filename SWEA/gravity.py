test = int(input())
for t in range(test):
    N = int(input())
    ls = list(map(int, input().split()))
    max_fall = 0
    for i in range(N-1):
        fall = len(list(filter(lambda x: ls[i] > x, ls[i+1:])))
        if fall > max_fall:
            max_fall = fall
    print(f'#{t+1} {max_fall}')
