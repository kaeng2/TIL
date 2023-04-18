

def solution(park, routes):
    R, C = len(park), len(park[0])
    movement = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }
    
    # 시작점을 찾는 함수   
    def find_start_point():
        for r in range(R):
            for c in range(C):
                if park[r][c] == "S":
                    return (r, c)

    # 실행 가능한 명령일 경우 이동한 위치를, 아닐 경우 원래의 위치를 반환하는 함수
    def execute_if_possible(route, now_i, now_j):
        D, N = route.split()
        nxt_i, nxt_j = now_i, now_j
        for n in range(int(N)):
            nxt_i += movement[D][0]
            nxt_j += movement[D][1]
            # 공원을 벗어난 경우     
            if nxt_i < 0 or R <= nxt_i or nxt_j < 0 or C <= nxt_j:
                return (now_i, now_j)
            # 장애물을 만난 경우
            if park[nxt_i][nxt_j] == "X":
                return (now_i, now_j)
        
        # 실행 가능한 경우 이동한 위치 반환
        return (nxt_i, nxt_j)
    
    # solve
    i, j = find_start_point()
    for route in routes:
        i, j = execute_if_possible(route, i, j)
    
    answer = [i, j]
    return answer