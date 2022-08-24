import sys
input = sys.stdin.readline
from collections import deque


# 도착 지점까지의 최소 이동 횟수를 반환하는 함수
def bfs():
    while Q:
        i, j = Q.popleft()                  # dequeue
        if (i, j) == (tg_i, tg_j):          # 출발 지점과 도착 지점이 같을 경우
            return 0
        for d in range(8):
            ni, nj = i + di[d], j + dj[d]
            if (ni, nj) == (tg_i, tg_j):    # 이동 가능한 지점 중에 도착 지점이 있으면 이동 횟수 반환
                return board[i][j]
            if 0 <= ni < L and 0 <= nj < L and not board[ni][nj]:  
                board[ni][nj] = board[i][j] + 1      # 다음 이동 지점까지의 이동 횟수 = 이전 지점까지의 이동 횟수 + 1
                Q.append((ni, nj))                   # enqueue


T = int(input())        # 테스트 케이스 개수
for _ in range(T):
    L = int(input())    # 체스판 한 변의 길이
    board = [[0]*L for _ in range(L)]   # 체스판
    now_i, now_j = map(int, input().split())    # 현재 위치 입력 받아 체스판에 표시
    board[now_i][now_j] = 1
    tg_i, tg_j = map(int, input().split())      # 목표 위치
    di, dj = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]   # 시계 방향
    Q = deque([(now_i, now_j)])     # queue에 출발 지점 enqueue
    min_move = bfs()                # 최소 이동 횟수 계산
    print(min_move)                 # 출력