# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # 색칠할 영역 개수
    N = int(input())
    # 10*10 배열
    rows = [[0]*10 for _ in range(10)]
    # info = [[r1, c1, r2, c2, color], [r1, c1, r2, c2, color], ...]
    info = [list(map(int, input().split())) for _ in range(N)]
    # 빨간색만 먼저 칠하기
    for red in list(filter(lambda x: x[-1] == 1, info)):
        # 영역 내의 각 행마다 해당하는 칸 1로 채우기
        for i in range(red[0], red[2]+1):
            rows[i][red[1]:red[3]+1] = [1]*(red[3]-red[1]+1)
    # 파란색 칠하기
    for blue in list(filter(lambda x: x[-1] == 2, info)):
        # 영역 내 칸을 순회하면서 값을 1씩 올려주기
        for i in range(blue[0], blue[2]+1):
            for j in range(blue[1], blue[3]+1):
                rows[i][j] += 1
    purple = 0
    # 전체 배열 중에 값이 2인 칸의 개수 구하기
    for row in rows:
        purple += len(list(filter(lambda x: x == 2, row)))
    print(f'#{t} {purple}')