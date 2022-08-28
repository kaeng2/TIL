import sys
input = sys.stdin.readline
from collections import deque


# S초 동안 바이러스를 증식시킨 후 필요한 위치의 바이러스 번호를 반환하는 함수
def grow_bfs():
    while Q:                            # Q가 빌 때까지
        i, j = Q.popleft()                  # 현재 출발점 설정
        if visited[i][j] == S+1:            # S초가 흐른 상태라면 X행 Y열의 바이러스 번호를 반환
            return germ[X-1][Y-1]
        for d in range(4):                  # 상하좌우에 빈 칸이 있다면 증식
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not germ[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1     # 1초가 흘렀다는 의미로 이 전 방문 체크 값에 1을 더해서 기록
                germ[ni][nj] = germ[i][j]               # 증식
                Q.append([ni, nj])                      # enqueue
    return germ[X-1][Y-1]               # S초가 흐르기 전에 가능한 증식이 모두 끝났다면 필요한 바이러스 번호 반환


N, K = map(int, input().split())                                # 시험관 크기, 바이러스 번호의 범위
germ = [list(map(int, input().split())) for _ in range(N)]      # 시험관의 세균 상태
S, X, Y = map(int, input().split())                             # 주어진 시간, S초 후 확인할 위치
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]                           # 상하좌우
visited = [[0] * N for _ in range(N)]
Q = deque()
# 출발점 설정
for k in range(1, K+1):                                         # 바이러스 번호가 작은 순서대로
    for x in range(N):
        for y in range(N):
            if germ[x][y] == k:
                Q.append([x, y])                                    # enqueue
                visited[x][y] = 1                                   # 방문 체크
print(grow_bfs())