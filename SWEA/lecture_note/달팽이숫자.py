# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # 배열 크기
    N = int(input())
    # 테스트 케이스 번호 출력
    print(f'#{t}')
    # 달팽이 숫자 배열을 기록할 리스트
    rows = [[0]*N for _ in range(N)]
    rows[0][0] = 1
    # 현재 위치
    i, j = 0, 0
    d = 0
    # 이동 방향에 따른 인덱스 변화
    # 우, 하, 좌, 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 지금 적어넣을 숫자
    order = 2
    # 모든 칸에 숫자를 다 채울 때까지
    while order <= N**2:
        # 다음 위치
        ni, nj = i + di[d%4], j + dj[d%4]
        # 다음 위치 인덱스가 유효하고 다음 칸이 0이라면
        # (단축평가 때문에 인덱스 에러 나지 않음)
        if ni in range(N) and nj in range(N) and rows[ni][nj] == 0:
            # 다음 위치로 이동하고 거기다 숫자 적어라
            i, j = ni, nj
            rows[i][j] = order
            # 숫자를 1 높인다
            order += 1
        # 다음 칸으로 이동할 수 없으면 방향을 바꿔라
        else:
            d += 1
    for row in rows:
        print(*row)