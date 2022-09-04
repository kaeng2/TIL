import sys
input = sys.stdin.readline

# T개의 테스트 케이스마다
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # M choose N 계산하기
    N = min(N, M-N)                 # M choose N = M choose (M-N)
    cases = 1
    for i in range(N):
        cases *= ((M-i) / (N-i))
    print(round(cases))             # 정수로 출력