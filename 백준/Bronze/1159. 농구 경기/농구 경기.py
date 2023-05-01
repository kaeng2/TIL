import sys
input = sys.stdin.readline
from collections import defaultdict

# 입력
N = int(input())
players = defaultdict(int)
for n in range(N):
    players[input()[0]] += 1

selected = [x for x in players if players[x] >= 5]
if selected:
    print(*sorted(selected), sep="")
else:
    print("PREDAJA")