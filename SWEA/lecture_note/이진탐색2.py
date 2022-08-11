def bin_search(lst, t):
    s, e = 0, len(lst)-1
    while s <= e:
        m = (s+e)//2
        if lst[m] == t:
            return m+1
        elif lst[m] < t:
            s = m + 1
        else:
            e = m - 1
    return 0

test = int(input())
for t in range(1, test+1):
    N, D = map(int, input().split())
    lst = list(map(int, input().split()))
    print(f'#{t} {bin_search(lst, D)}')