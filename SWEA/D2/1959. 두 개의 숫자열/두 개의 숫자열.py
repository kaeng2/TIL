test = int(input())
for t in range(1, test+1):
    N, M = map(int, input().split())
    Ai = [int(x) for x in input().split()]
    Bj = [int(y) for y in input().split()]
    result = []
    if N < M:
        for start in range(M-N+1):
            cut_Bj = Bj[start: start+N]
            result += [sum(map(lambda x,y: x*y, Ai, cut_Bj))]
    elif N > M:
        for start in range(N-M+1):
            cut_Ai = Ai[start: start+M]
            result += [sum(map(lambda x,y: x*y, cut_Ai, Bj))]
    print(f'#{t} {max(result)}')