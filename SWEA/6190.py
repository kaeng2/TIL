test = int(input())
for t in range(1, test+1):
    N = int(input())
    num = list(map(int, input().split()))
    num.sort(reverse=True)
    for i in range(N):
        for j in range(i+1, N):
            if list(str(num[i]*num[j])) == sorted(str(num[i]*num[j])):
                mono_inc = num[i]*num[j]
                break
        else:
            continue
        break
    print(f'#{t} {mono_inc}')
