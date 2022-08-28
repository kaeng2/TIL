import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)


# 하루 동안의 인구 이동을 진행하는 함수
def bfs():
    global day                              # 인구 이동이 지속되는 기간
    visited = [[0] * N for _ in range(N)]   # 방문 체크
    k = 0                                   # 오늘 인구 이동을 진행할 연합이 없다면 0, 있다면 1 이상
    for a in range(N):
        for b in range(N):                              # 모든 좌표를 순회하면서
            if not visited[a][b]:                           # 미방문한 곳이 있다면 연합의 가능성이 있으므로 
                union.clear()
                Q.append([a, b])                            # enqueue
                union.append([a, b])                        # 연합에 넣어주고
                union_pp, union_cnt = popl[a][b], 1         # 연합국의 총 인구수, 연합국 개수 세팅
                while Q:                                    # Q가 빌 때까지
                    i, j = Q.popleft()                          # 현재 좌표 설정       
                    visited[i][j] = 1                           # 방문 체크
                    for d in range(4):                          # 상하좌우 중 연합국이 있다면
                        ni, nj = i + di[d], j + dj[d]
                        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(popl[i][j] - popl[ni][nj]) <= R:
                            visited[ni][nj] = 1                     # 방문 체크하고
                            union_pp += popl[ni][nj]                # 연합국 총 인구수를 더해주고
                            union_cnt += 1                          # 연합국 개수를 올려주고
                            Q.append([ni, nj])                      # enqueue                
                            union.append([ni, nj])                  # 연합에 넣어주고
                            k += 1                                  # 오늘 인구 이동이 있다는 뜻으로 k를 올려준다
                if union_cnt > 1:                           # 검사가 끝났을 때 연합국이 2개 이상이면
                    p = union_pp // union_cnt                   # 연합국의 인구 이동 진행
                    for x, y in union:
                        popl[x][y] = p
    if not k:       # 모든 좌표 순회가 끝났을 때 인구 이동을 진행할 연합이 하나도 없다면 종료
        return
    day += 1        # 종료 조건을 만족하지 않았을 경우 기간을 +1 해주고
    bfs()           # 다음 날의 인구 이동 진행


N, L, R = map(int, input().split())                                 # 땅의 크기, 인구 이동 최소 제한, 최대 제한
popl = [list(map(int, input().split())) for _ in range(N)]          # 인구 정보
day = 0                                                             # 인구 이동이 지속되는 기간
Q, union = deque(), deque()                                         # bfs 이동을 위한 queue, 연합국 기록을 위한 queue
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]                               # 상하좌우
bfs()                                                               # 인구 이동 진행
print(day)                                                          # 출력