import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poketmon = {}
for n in range(1, N+1):
    name = input().rstrip()
    poketmon[str(n)] = name
    poketmon[name] = n
for _ in range(M):
    print(poketmon[input().rstrip()])