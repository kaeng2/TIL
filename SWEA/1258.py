# 사각형을 검사할 시작 좌표를 입력하면
# 사각형의 행 개수(height), 열 개수(width), 크기(width*height)를 반환해주고
# 감지한 사각형 내부를 모두 0으로 만들어주는 함수
def square_info(start_row, start_col):
    # 행 개수 조사하기
    # 현재 위치에서 수직으로 내려가면서 행 개수를 세다가
    # 0이 나오면 반복문 종료
    height = 1
    for current_location in range(start_row, n-1):
        if storage[current_location+1][start_col]:
            height += 1
        else:
            break
    # 같은 방식으로 열 개수 조사하기
    width = 1
    for current_location in range(start_col, n-1):
        if storage[start_row][current_location+1]:
            width += 1
        else:
            break
    # 사각형 내부를 전부 0으로 변환 (반복 탐지 방지)
    def clean(start_row, start_col):
        for row in range(start_row, start_row+height):
            storage[row][start_col:start_col+width] = [0]*width
    clean(start_row, start_col)
    return height, width, width*height

# 테스트 케이스의 개수
test = int(input())
# 각 테스트 케이스마다
for test_num in range(test):
    # n 차원 배열
    n = int(input())
    # storage = [[첫째 행], [둘째 행], ...]
    storage = [list(map(int, input().split())) for _ in range(n)]
    squares = []
    # (0, 0)부터 (n, n)까지 차례대로 검사
    for i in range(n):
        for j in range(n):
            # 0이 아닌 값이 발견되면 사각형을 검사하고 사각형 내부 청소
            if storage[i][j]:
                # 반환한 사각형 정보 값은 squares 리스트에 튜플 형태로 저장
                squares += [square_info(i, j)]
    # 저장된 사각형 정보들을 정렬
    # 넓이가 작은 것부터 정렬한 후, 행 개수가 작은 것부터 정렬
    squares.sort(key=lambda x: (x[-1], x[0]))
    # 테스트 케이스 번호와 사각형 개수 출력
    print(f'#{test_num+1} {len(squares)}', end=' ')
    # 각 사각형의 행 개수와 열 개수를 한 줄로 출력하고 다하면 줄바꿈
    for idx in len(squares):
        print(squares[idx][0], squares[idx][1], end=' ')
    print()

