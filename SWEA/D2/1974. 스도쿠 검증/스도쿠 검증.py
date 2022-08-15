def check(rows, cols, blocks):
    for row in rows:
        if len(set(row)) != 9:
            return 0
    for col in cols:
        if len(set(col)) != 9:
            return 0
    for block in blocks:
        if len(set(block)) != 9:
            return 0
    else:
        return 1
    
test = int(input())
for t in range(1, test+1):
    print(f'#{t}', end=' ')
    # rows = [[첫째 행], [둘째 행], ...]
    rows = [list(map(int, input().split())) for _ in range(9)]            
    # cols = [(첫째 열), (둘째 열), ...]
    cols = list(zip(*rows))
    # blocks = [[첫째 블럭], [둘째 블럭], ...]
    blocks = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            blocks += [rows[i][j:j+3] + rows[i+1][j:j+3] + rows[i+2][j:j+3]]
    print(check(rows, cols, blocks))