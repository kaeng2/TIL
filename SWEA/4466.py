test = int(input())
for t in range(1, test+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    grade = sum(scores[:K])
    print(f'#{t} {grade}')
    