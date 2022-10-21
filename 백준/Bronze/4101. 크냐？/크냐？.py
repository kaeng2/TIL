import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    ans = {a: 'Yes', b: 'No'}
    print(ans[max(a, b)])