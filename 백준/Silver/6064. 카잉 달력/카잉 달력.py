import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    # M과 N의 최소공배수 구하기 (카잉 달력의 마지막 해)
    a, b = max(M, N), min(M, N)
    for common_mul in range(a, a*b+1, a):
        if common_mul % b == 0:
            break
    # <x:y>가 몇 번째 해인지 구하기
    for k in range(x, common_mul+1, M):     
        if k % N == y % N:                     
            print(k)
            break
    else:
        print(-1)