import sys
input = sys.stdin.readline
from collections import deque


# 입력
N, M = map(int, input().split())                                                    # 행 개수, 열 개수
cheese = [list(map(int, input().split())) for _ in range(N)]                        # 치즈 정보
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]                                               # 상하좌우 이동
visited = [[1] * M] + [[1] + [0] * (M-2) + [1] for _ in range(N-2)] + [[1] * M]     # 방문 기록 (테두리는 모두 방문 처리)
# 출발점 설정
Q = deque()
for i in [0, N-1]:                                                                  # 테두리의 모든 좌표 enqueue
    for j in range(M):
        Q.append([i, j])
for j in [0, M-1]:
    for i in range(1, N-1):
        Q.append([i, j])
# 탐색
while Q:
    i, j = Q.popleft()
    for d in range(4):                                                              # 상하좌우 중 이동 가능한 방향에 대해
        ni, nj = i + di[d], j + dj[d]
        if 1 <= ni < N-1 and 1 <= nj < M-1 and not visited[ni][nj]:
            if cheese[ni][nj]:                                                          # 치즈면
                visited[ni][nj] = visited[i][j] + 1                                         # 이전 칸 +1 기록
                Q.append([ni, nj])                                                          # 맨 뒤에 enqueue
            else:                                                                       # 빈 칸이면
                visited[ni][nj] = visited[i][j]                                             # 시간이 흐르지 않음
                Q.appendleft([ni, nj])                                                      # 맨 앞에 enqueue
# 정답 계산
ans = 0
for row in visited:
    ans = max(ans, *row)
print(ans-1)                        # 총 걸린 시간
last_cheese = 0
for x in range(1, N-1):
    for y in range(1, M-1):
        if cheese[x][y] and visited[x][y] == ans:
            last_cheese += 1
print(last_cheese)                  # 마지막에 녹은 치즈의 개수