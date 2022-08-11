test = int(input())
for t in range(1, test+1):
    N = int(input())
    rows = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    sm = 0
    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < N and 0 <= nj < N:
                    sm += abs(rows[i][j] - rows[ni][nj])
    print(f'#{t} {sm}')