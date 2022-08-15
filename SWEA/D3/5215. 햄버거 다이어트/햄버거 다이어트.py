test = int(input())
for t in range(1, test+1):
    N, L = map(int, input().split())
    ingr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    for i in range(1, 2**N):
        favor, calories = 0, 0
        for j in range(N):
            if i & 1 << j:
                favor += ingr[j][0]
                calories += ingr[j][1]
        if calories > L:
            continue
        else:
            if mx < favor:
                mx = favor
    print(f'#{t} {mx}')