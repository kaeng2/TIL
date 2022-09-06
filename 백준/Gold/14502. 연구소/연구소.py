import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations


# 안전 영역 크기의 최대값을 반환하는 함수
def bfs():
    safe_zone = deque()                             # 벽을 세울 때마다 안전 영역의 크기를 기록하는 배열
    for walls in combinations(blank, 3):            # 빈 칸 중에 3개를 골라서 벽을 세운다
        visited = [[0] * M for _ in range(N)]           # 벽을 세울 때마다 방문 배열 초기화
        for a, b in walls:
            visited[a][b] = 1                               # 벽을 세운 위치에는 전염되지 않도록 방문 표시
        Q = deque(virus)                                # 바이러스 전염 시작
        while Q:
            now_i, now_j = Q.popleft()
            for d in range(4):                                  # 상하좌우 중 미방문한 빈칸에 전파
                nxt_i, nxt_j = now_i + di[d], now_j + dj[d]
                if 0 <= nxt_i < N and 0 <= nxt_j < M and not lab[nxt_i][nxt_j] and not visited[nxt_i][nxt_j]:
                    visited[nxt_i][nxt_j] = 1                       # 방문 처리
                    Q.append((nxt_i, nxt_j))                        # enqueue
        safe = 0
        for x in range(N):                                  # 빈칸인데 전파하지 못한 곳을 발견하면 safe +1
            for y in range(M):
                if not lab[x][y] and not visited[x][y]:
                    safe += 1
        safe_zone.append(safe)                              # safe_zone에 안전 영역 크기 기록
    return max(safe_zone)           # 안전 영역 크기 중 최대값 반환


N, M = map(int, input().split())                                # 지도의 세로 크기, 가로 크기
lab = [list(map(int, input().split())) for _ in range(N)]       # 지도 모양
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]                           # 상하좌우
virus = deque()
blank = deque()
for i in range(N):                      # 연구소 전체를 순회하면서
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i, j))            # 바이러스의 위치 기록
        elif lab[i][j] == 0:
            blank.append((i, j))            # 빈 칸의 위치 기록 (벽을 세울 수 있는 위치)
print(bfs())