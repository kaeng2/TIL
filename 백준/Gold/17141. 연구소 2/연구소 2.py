import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque


# 바이러스가 퍼지는 데 걸리는 최소 시간을 반환하는 함수 (불가능하면 None 반환)
def spread():
    while Q:
        i, j = Q.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and not lab[ni][nj] % 2:
                visited[ni][nj] = visited[i][j] + 1
                Q.append([ni, nj])
    for x in range(N):                                      # 바이러스가 퍼지지 못한 칸이 있는지 검사
        for y in range(N):
            if not lab[x][y] % 2 and not visited[x][y]:
                return
    return visited[i][j] - 1


N, M = map(int, input().split())    # 연구소의 크기, 놓을 수 있는 바이러스의 개수
lab = [list(map(int, input().split())) for _ in range(N)]
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
virus_able = deque()
for i in range(N):                      # 바이러스를 놓을 수 있는 좌표 리스트
    for j in range(N):
        if lab[i][j] == 2:
            virus_able.append([i, j])
Q, record = deque(), deque()
for init in combinations(virus_able, M):            # 가능한 바이러스 초기 위치마다
    visited = [[0] * N for _ in range(N)]               # 방문 체크 초기화
    for x, y in init:
        Q.append([x, y])                                # enqueue
        visited[x][y] = 1                               # 방문 체크
    record.append(spread())                             # 확산 시간 계산
record = [res for res in record if res is not None]     # 유효한 시간만 필터링
if record:
    print(min(record))
else:                                               # 모든 경우의 수에서 확산에 실패한 경우
    print(-1)