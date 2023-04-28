import sys
input = sys.stdin.readline

a, b = map(lambda x: int(x, 2), input().split())
print(format(a+b, 'b'))