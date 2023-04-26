import sys
input = sys.stdin.readline

# 입력
X = int(input())

stick = 64
ans = 0
while X > 0:
    if stick > X:
        stick //= 2
    else:
        X -= stick
        ans += 1
print(ans)