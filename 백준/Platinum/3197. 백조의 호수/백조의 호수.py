import sys
input = sys.stdin.readline
from collections import deque

'''
1. 백조 이동
    - move_now에 있는 좌표들에 대해서
        - 상하좌우 중 인덱스가 유효하고 미방문 한 칸이 있으면
            - 일단 방문 처리
            
            - 물이라면 이동
                1. move_now 큐에 enqueue
            - 얼음이라면 다음 차례에 이동할 수 있는 곳이니까 따로 저장
                1. move_nxt 큐에 enqueue
            - 백조를 만나면
                1. True 반환하며 종료
    
    - 백조를 못 만난 채로 탐색이 종료되면
        - move_nxt에 넣어놨던 좌표들 move_now로 옮겨두기 (다음 이동을 위해서)
        - False 반환하며 종료

2. 1번에서 백조를 못 만났다면 얼음 녹이기
    - melt_now 큐에 있는 좌표들에 대해서
        - 인접한 좌표 중 얼음을 만나면
            1. 'X'를 '.'로 변환해준다. (녹았다는 표시)
            1. melt_nxt 큐에 enqueue
            2. 방문 처리
    - 얼음을 다 녹이고 나면 melt_nxt에 넣어놨던 좌표들 melt_now로 옮겨두기 (다음 해빙을 위해서)
    - 소요된 날 수를 1 올려준다.

백조가 서로 만날 때까지 이 사이클을 반복한다.
백조가 만나면 소요된 날 수를 출력하고 사이클을 종료한다.    
'''


def swan_moves():
    global move_now
    move_nxt = deque()
    while move_now:
        i, j = move_now.popleft()

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj]:
                visited[ni][nj] = 1
                if lake[ni][nj] == '.':
                    move_now.append((ni, nj))
                elif lake[ni][nj] == 'X':
                    move_nxt.append((ni, nj))
                else:
                    return True
    move_now = deque(move_nxt)
    return False


def melt():
    melt_nxt = deque()
    while melt_now:
        i, j = melt_now.popleft()

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]

            if 0 <= ni < R and 0 <= nj < C and lake[ni][nj] == 'X' and not melted[ni][nj]:
                lake[ni][nj] = '.'
                melt_nxt.append((ni, nj))
                melted[ni][nj] = 1
    return melt_nxt


# 입력
R, C = map(int, input().split())
lake = [list(input()) for _ in range(R)]

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0] * C for _ in range(R)]   # 백조 방문 배열
melted = [[0] * C for _ in range(R)]    # 얼음 방문 배열
move_now, melt_now = deque(), deque()

for x in range(R):
    for y in range(C):
        # 물 좌표
        if lake[x][y] != 'X':
            for d in range(4):
                nx, ny = x + di[d], y + dj[d]
                if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == 'X':     # 얼음과 인접해 있다면
                    melt_now.append((x, y))                                     # 이번에 녹일 큐에 추가
                    melted[x][y] = 1                                            # 방문 처리
                    break                                                       # 한 면이라도 인접하면 더 볼 필요 없음
        # 백조 좌표
        if lake[x][y] == 'L' and not move_now:    # 백조 한 마리만 enqueue
            move_now.append((x, y))
            visited[x][y] = 1                           # 방문 처리

day = 0
while True:
    # 백조 이동
    met = swan_moves()

    if not met:                 # 백조가 못 만났으면
        melt_now = deque(melt())    # 얼음 녹이고
        day += 1                    # 지난 날 수 세주기
    else:                       # 만났으면
        print(day)                  # 지난 날 수 출력
        break                       # 종료