from collections import deque

N, M = map(int, input().split())                      # 행 개수, 열 개수
maze = [list(map(int, input())) for _ in range(N)]    # 미로 배열
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]                 # 상하좌우 이동
visited = [[0] * M for _ in range(N)]                 # 방문 기록
Q = deque()
visited[0][0] = 1                                     # 출발점 설정
Q.append([0, 0])
while Q:
    i, j = Q.popleft()
    for d in range(4):                                # 상하좌우 중 이동 가능한 방향에 대해
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and maze[ni][nj]:
            visited[ni][nj] = visited[i][j] + 1           # 이전 칸 + 1 기록 (이동 거리)
            if (ni, nj) == (N-1, M-1):                    # 도착점에 도착하면 반복문 종료
                Q.clear()
            else:
                Q.append([ni, nj])                          
print(visited[N-1][M-1])                              # 출력