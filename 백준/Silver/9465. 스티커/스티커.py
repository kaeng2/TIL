# 테스트 케이스 개수
T = int(input())
# 각 테스트 케이스마다
for t in range(T):
    # 입력
    n = int(input())
    rows = [list(map(int, input().split())) for _ in range(2)]
    # 스티커가 한 줄 밖에 없으면 윗 칸, 아래 칸 비교해서 최대값 출력
    if n == 1:
        print(max(rows[0][0], rows[1][0]))
    else:
        # 최대값 리스트
        # mx[0][i]는 (i+1)번째 열 중 윗 칸까지 왔을 때의 최대값
        # mx[1][i]는 (i+1)번째 열 중 아래 칸까지 왔을 때의 최대값
        mx = [[0]*n, [0]*n]
        # 초기값 설정
        mx[0][:2] = [rows[0][0], rows[1][0] + rows[0][1]]
        mx[1][:2] = [rows[1][0], rows[0][0] + rows[1][1]]
        # 점화식 이용 하여 최대값 리스트 채우기
        for i in range(2, n):
            mx[0][i] = max(mx[1][i-1], mx[1][i-2]) + rows[0][i]
            mx[1][i] = max(mx[0][i-1], mx[0][i-2]) + rows[1][i]
        # 출력
        print(max(mx[0][n-1], mx[1][n-1]))