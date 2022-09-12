import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations

N, M = map(int, input().split())
nums = map(int, input().split())
ans = deque()
for seq in permutations(nums, M):
    ans.append(seq)
ans = sorted(set(ans))
for seq in ans:
    print(*seq)