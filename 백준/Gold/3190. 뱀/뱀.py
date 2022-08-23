# 입력
N = int(input())                        # 보드 크기
board = [[0] * N for _ in range(N)]     # 보드판
board[0][0] = 2                         # 출발점 표시
K = int(input())                        # 사과 개수
for _ in range(K):                      # 사과 위치 표시
    i, j = map(int, input().split())
    board[i-1][j-1] = 3
l = int(input())                        # 방향 변환 횟수
turn = {}
for _ in range(l):                      # 방향 변환 정보 기록
    x, y = input().split()
    turn[int(x)] = y

# 필요한 변수 생성
di, dj = [0, -1, 0, 1], [1, 0, -1, 0]       # 우, 상, 좌, 하
h_sec, t_sec = 0, 0                         # 머리의 이동 칸 수, 꼬리의 이동 칸 수
hi, hj, hd, ti, tj, td = 0, 0, 0, 0, 0, 0   # 머리 좌표, 머리 이동 방향, 꼬리 좌표, 꼬리 이동 방향

# 게임 시작
while True:
    if turn.get(h_sec) == 'L':              # 머리 좌회전
        hd = (hd+1) % 4
    elif turn.get(h_sec) == 'D':            # 머리 우회전
        hd = (hd+3) % 4
    ni, nj = hi + di[hd], hj + dj[hd]       # 다음 이동 좌표
    if 0 <= ni < N and 0 <= nj < N and board[ni][nj] % 3 == 0:  # 다음 이동 좌표가 유효하고, 빈 칸이거나 사과가 있을 경우
        hi, hj = ni, nj                                             # 머리 이동
        if board[hi][hj] != 3:                                      # 빈 칸인 경우
            board[ti][tj] = 0                                           # 꼬리 지우고
            if turn.get(t_sec) == 'L':                                  # 꼬리 이동 방향 설정
                td = (td+1) % 4
            elif turn.get(t_sec) == 'D':
                td = (td+3) % 4
            ti, tj = ti + di[td], tj + dj[td]                           # 꼬리 이동
            t_sec += 1                                                  # 꼬리 이동 칸 수 1 올려주기
        board[hi][hj] = 2                                           # 머리 표시
    else:                                                       # 벽이나 자기 몸에 부딪히는 경우 종료 
        break
    h_sec += 1                                                  # 모든 이동 후 머리 이동 칸 수 1 올려주기

# 출력
print(h_sec + 1)