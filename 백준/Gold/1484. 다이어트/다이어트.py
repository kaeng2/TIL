import sys
input = sys.stdin.readline


G = int(input())
s, e = 1, 1
ans = []
while s <= e:
    if e**2 - (e-1)**2 > G:
        break
    result = e**2 - s**2
    if result < G:
        e += 1
    else:
        s += 1
        if result == G:
            ans += [e]
if ans:
    print(*ans, sep='\n')
else:
    print(-1)