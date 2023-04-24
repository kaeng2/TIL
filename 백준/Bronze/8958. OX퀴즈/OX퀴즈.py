import sys
input = sys.stdin.readline

N = int(input())
for n in range(N):
    quiz = input().rstrip().split("X")
    score = 0
    for O_str in quiz:
        O_num = len(O_str)
        score += O_num * (1 + O_num) // 2    # 1 + ... + O_num
    print(score)