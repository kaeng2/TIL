### 내장 sum, max 함수 없이 풀기!

# iterable 내의 숫자형 자료의 합을 구하는 함수 정의
def my_sum(iterables):
    result = 0
    for elem in iterables:
        result += elem
    return result


# iterable 내의 숫자형 자료의 최대값을 구하는 함수 정의
def my_max(iterables):
    result = -10e9
    for elem in iterables:
        if result < elem:
            result = elem
    return result


for _ in range(10):
    test = int(input())
    rows = [list(map(int, input().split())) for _ in range(100)]
    cols = zip(*rows)
    # 최대값을 저장할 변수
    mx = 0
    # 각 행의 합이 현재 최대값보다 크면 최대값 갱신
    for row in rows:
        if mx < my_sum(row):
            mx = my_sum(row)
    # 각 열의 합이 현재 최대값보다 크면 최대값 갱신
    for col in cols:
        if mx < my_sum(col):
            mx = my_sum(col)
    # 두 대각선 각각의 합을 구하고 최대값 갱신
    diag1, diag2 = 0, 0
    for i in range(100):
        diag1 += rows[i][i]
        diag2 += rows[i][99 - i]

    print(f'#{test} {my_max([mx, diag1, diag2])}')