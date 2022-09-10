import sys
input = sys.stdin.readline
from collections import deque

'''
실제 구역 개수를 탐색한 후, 적록색약이 보는 구역의 개수를 탐색한다. 
bfs로 전체 배열을 탐색하면서 구역의 개수를 세면서 동시에 초록색 칸은 빨간색 칸으로 바꿔준다.
최초 탐색이 끝나고 나면 전체 배열은 빨간색과 파란색으로만 이루어지게 된다.
따라서 한 번 더 탐색하면 적록색약이 보는 구역의 개수를 계산할 수 있다.
'''


# 구역의 개수를 반환하는 함수
def bfs():
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]       # 상하좌우 이동
    visited = [[0] * N for _ in range(N)]       # 방문 배열
    area = 0                                    # 구역의 개수
    for x in range(N):                          # 전체 좌표를 순회하다가
        for y in range(N):
            if not visited[x][y]:                   # 미방문 지점을 발견하면
                # 탐색 구역 정보와 구역의 개수 업데이트
                color = picture[x][y]                   # 현재 구역의 색깔
                area += 1                               # 구역의 개수 +1

                # bfs 탐색
                Q = deque([[x, y]])                     # 출발점 enqueue
                visited[x][y] = 1                       # 출발점 방문 처리
                while Q:                                # Q가 빌 때까지
                    i, j = Q.popleft()                      # 현재 좌표
                    if color == 'G':                        # 현재 칸이 초록색이면 빨간색으로 바꿔준다
                        picture[i][j] = 'R'
                    for d in range(4):                      # 상하좌우로 인접한 좌표 중 현재 구역 색깔과 일치하면서 미방문한 좌표가 있다면
                        ni, nj = i + di[d], j + dj[d]
                        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and picture[ni][nj] == color:
                            Q.append([ni, nj])                  # enqueue
                            visited[ni][nj] = 1                 # 방문 처리
    return area     # 전체 구역 개수 반환


N = int(input())
picture = [list(input().rstrip()) for _ in range(N)]
ans = [bfs(), bfs()]    # [실제 구역 개수, 적록색약이 보는 구역의 개수]
print(*ans)