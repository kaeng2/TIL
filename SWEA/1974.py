# 모든 행별로, 열별로, 블럭별로 중복된 숫자가 있는지 검사해주는 함수
# 차례대로 진행하다가 중복된 숫자가 나오는 순간 0을 반환한다.
# 중복된 숫자가 안나오고 for문이 무사히 종료되면 1을 반환한다.
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

# 테스트 케이스 개수    
test = int(input())
# 테스트 케이스마다
for t in range(1, test+1):
    # 테스트 케이스 번호부터 출력하고
    print(f'#{t}', end=' ')
    
    # 함수의 인자로 넣어줄 행 리스트, 열 리스트, 블럭 리스트를 만들어준다
    # rows = [[첫째 행], [둘째 행], ...]
    rows = [list(map(int, input().split())) for _ in range(9)]            
    # cols = [(첫째 열), (둘째 열), ...]
    cols = list(zip(*rows))
    # blocks = [[첫째 블럭], [둘째 블럭], ...]
    blocks = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            blocks += [rows[i][j:j+3] + rows[i+1][j:j+3] + rows[i+2][j:j+3]]

    # 결과값을 출력한다
    print(check(rows, cols, blocks))
