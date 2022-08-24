import sys
from collections import deque
input = sys.stdin.readline

# tomato 배열에 각 토마토가 며칠 째에 익었는지 표시해주는 함수
def bfs(init):
    while init:
        i, j = init.popleft()
        for d in range(4):              # 인접한 토마토 중 익지 않은 토마토가 있다면
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not tomato[ni][nj]:
                tomato[ni][nj] = tomato[i][j] + 1      # 익은 상태로 변환
                init.append((ni, nj))       # 새롭게 익은 토마토 위치 리스트에 추가


# 입력
M, N = map(int, input().split())                                # 열 개수, 행 개수
tomato = [list(map(int, input().split())) for _ in range(N)]    # 토마토 상태

# 처음부터 모든 토마토가 익어있는 상태인지 확인
for row in tomato:
    if 0 in row:    # 안 익은 토마토가 발견될 경우 not done
        done = 0
        break
else:               # 모든 토마토가 익어있는 경우 done
    print(0)
    done = 1

# 안 익은 토마토가 있는 경우
if not done:
    # 토마토 익히기
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]       # 상하좌우 확인
    Q = deque()                                 # 인접 토마토에 영향을 줄 토마토 위치
    for i in range(N):                          # 이미 익어있는 토마토 위치 저장
        for j in range(M):
            if tomato[i][j] == 1:
                Q += [(i, j)]
    bfs(Q)                                      # 숙성!
    # 걸린 기간 계산
    mx = 0
    for row in tomato:
        if 0 in row:            # 여전히 익지 않은 토마토가 있다면 -1 출력
            print(-1)
            break
        mx = max(mx, max(row))  # 최대값 찾기
    else:
        print(mx-1)             # 안 익은 토마토가 없다면 최대값 출력 (맨 처음 이미 익어있던 토마토 값이 1이었기 때문에 1을 빼준다)
