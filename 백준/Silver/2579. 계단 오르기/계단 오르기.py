import sys
input = sys.stdin.readline

n = int(input())
stairs = [0, 0, 0] + [int(input()) for _ in range(n)]
max_scores_at = [0 for _ in range(n+3)]
for i in range(3, n+3):
    max_scores_at[i] = stairs[i] + max(
        max_scores_at[i-2],
        stairs[i-1] + max_scores_at[i-3]
    )

print(max_scores_at[-1])