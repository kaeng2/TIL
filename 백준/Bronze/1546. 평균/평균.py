import sys
input = sys.stdin.readline


# 입력
N = int(input())
scores = list(map(int, input().split()))

new_average = (sum(scores) / N) * 100 / max(scores)
print(new_average)