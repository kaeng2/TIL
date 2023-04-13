import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())        # 방 크기
r, c, dir = map(int, input().split())     # 청소기 위치, 방향
room = [list(map(int, input().split())) for _ in range(N)]  # 방 상태

cleaned_room = 0
directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

def clean_current_space(n, m, d):
    global cleaned_room
    
    # 현재 칸 청소
    if room[n][m] == 0:
        cleaned_room += 1
        room[n][m] = 2
    
    # 주변 칸 청소
    for turn in range(3, -1, -1):
        delta_n, delta_m = directions[(d+turn)%4]
        
        # 인덱스가 유효하고, 벽이 아니고, 청소가 안 되어있는 경우에만 전진해서 청소
        if 0 < n + delta_n < N-1 and 0 < m + delta_m < M-1 and room[n + delta_n][m + delta_m] == 0:
            clean_current_space(n + delta_n, m + delta_m, (d+turn)%4)
            return
        
        # 주변에 청소 안 된 칸이 없으면 후진
        if turn == 0:
            # 후진 못하면 종료
            if n - delta_n == 0 | N-1 or m - delta_m == 0 | M-1 or room[n - delta_n][m - delta_m] == 1:
                return
            clean_current_space(n - delta_n, m - delta_m, d)
    
    return

clean_current_space(r, c, dir)
print(cleaned_room)
