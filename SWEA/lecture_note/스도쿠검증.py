# 스도쿠가 정답인지 체크하는 함수
def check_sudoku(rows):
    # 행 별로 확인
    for row in rows:
        if len(set(row)) != 9:
            return 0
    # 열 별로 확인
    cols = list(zip(*rows))
    for col in cols:
        if len(set(col)) != 9:
            return 0
    # 각 블럭마다 확인
    for j in [0, 3, 6]:
        for i in [0, 3, 6]:
            block = []
            block += rows[i][j:j + 3] + rows[i+1][j:j + 3] + rows[i+2][j:j + 3]
            if len(set(block)) != 9:
                return 0
    return 1


test = int(input())
for t in range(1, test+1):
    rows = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t} {check_sudoku(rows)}')

