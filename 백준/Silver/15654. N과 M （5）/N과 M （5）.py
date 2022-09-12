import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
for seq in permutations(nums, M):
    print(*seq)