import sys
input = sys.stdin.readline
from collections import deque

# 섬의 총 개수를 반환하는 함수
def bfs():
    visited = [[0] * w for _ in range(h)]                               # 방문 배열
    di, dj = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]   # 왼쪽 대각선 위부터 시계 방향으로 탐색
    Q = deque()                                                             
    island = 0          # 섬의 개수
    # 섬 탐색
    for x in range(h):
        for y in range(w):
            if land[x][y]:              # 섬이 발견되면
                visited[x][y] = 1           # 방문 체크
                island += 1                 # 섬 개수 +1
                # 해당 섬 탐색 시작
                Q.append([x, y])            
                while Q:
                    i, j = Q.popleft()
                    for d in range(8):                      # 같은 섬인 칸이 있다면
                        ni, nj = i + di[d], j + dj[d]
                        if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and land[ni][nj]:
                            visited[ni][nj] = 1                 # 방문 체크
                            land[ni][nj] = 0                    # 섬 지우기
                            Q.append([ni, nj])                  # enqueue
    # 모든 탐색이 끝나면 섬 개수 반환
    return island


while True:
    w, h = map(int, input().split())
    if not w and not h:     # 0 0이 입력되면 종료
        break
    land = [list(map(int, input().split())) for _ in range(h)]
    print(bfs())