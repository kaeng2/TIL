import sys
input = sys.stdin.readline
from collections import deque


# 필요한 배추흰지렁이의 마리 수를 출력하는 함수
def bfs():
    visited = [[0] * M for _ in range(N)]   # 방문 배열
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상하좌우 탐색
    Q = deque()
    worm = 0                                # 지렁이 마리 수
    # 배추밭 탐색
    for x in range(N):                      # 밭 전체를 순회하면서
        for y in range(M):
            if field[x][y]:                     # 배추가 발견되면
                visited[x][y] = 1               # 방문 체크
                worm += 1                       # 지렁이 개수 +1
                # 연결된 배추 탐색 시작
                Q.append([x, y])
                while Q:
                    i, j = Q.popleft()
                    for d in range(4):                      # 연결된 배추가 있다면
                        ni, nj = i + di[d], j + dj[d]
                        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and field[ni][nj]:
                            visited[ni][nj] = 1                 # 방문 체크
                            field[ni][nj] = 0                   # 배추 지우기
                            Q.append([ni, nj])                  # enqueue

    # 모든 탐색이 끝나면 지렁이 마리 수 출력 후 종료
    print(worm)
    return worm


# T개의 테스트 케이스
T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())     # 밭의 가로 길이, 세로 길이, 배추의 수
    # 배추밭 기록
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    # 계산 및 출력
    bfs()