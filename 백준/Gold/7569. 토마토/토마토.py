import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    # 초기 세팅
    di, dj, dk = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, 1, -1]  # 상, 하, 좌, 우, 윗층, 아랫층
    Q = deque()
    day = [[[0] * M for _ in range(N)] for _ in range(H)]   # 해당 토마토가 몇 번째 날에 익었는지 기록
    # 출발점 설정
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[k][i][j] == 1:    # 익은 토마토를 찾아서
                    Q.append([i, j, k])         # 좌표 enqueue
                    day[k][i][j] = 1            # 첫째 날에 익은 것으로 설정
    while Q:
        i, j, k = Q.popleft()
        for d in range(6):      # 인접한 토마토 중 안 익은 토마토가 있다면
            ni, nj, nk = i + di[d], j + dj[d], k + dk[d]
            if 0 <= ni < N and 0 <= nj < M and 0 <= nk < H and not tomato[nk][ni][nj] and not day[nk][ni][nj]:
                tomato[nk][ni][nj] = 1                  # 숙성
                day[nk][ni][nj] = day[k][i][j] + 1      # 몇 번째 날에 익었는지 기록
                Q.append([ni, nj, nk])                  # enqueue

    ans = 0
    for k in range(H):
        for i in range(N):
            if 0 in tomato[k][i]:               # 숙성 과정이 끝났을 때 안 익은 토마토가 있는 경우
                return -1                           # -1 반환
            ans = max(ans, max(day[k][i]))      # 가장 마지막에 익은 토마토가 몇 번째 날에 익었는지 찾는다
    return ans-1                            # 모두 익는데 걸린 기간 반환


# 입력
M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# 계산 및 출력
print(bfs())