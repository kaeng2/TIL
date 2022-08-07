# 90도 돌리는 함수
def turn90(cols):
    turn90 = []
    for col in cols:
        turn90 += [''.join(reversed(list(map(str, col))))]
    return turn90

# 180도 돌리는 함수
def turn180(rows):
    turn180 = []
    for row in reversed(rows):
        turn180 += [''.join(reversed(list(map(str, row))))]
    return turn180

# 270도 돌리는 함수
def turn270(cols):
    turn270 = []
    for col in reversed(cols):
        turn270 += [''.join(map(str, col))]
    return turn270

# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
	# 행렬의 차원
    N = int(input())
	# 행과 열 입력
    rows = [list(map(int, input().split())) for _ in range(N)]
    cols = list(zip(*rows))
    # 90도, 180도, 270도 돌린 결과를 별도의 변수에 저장
    rot90 = turn90(cols)
    rot180 = turn180(rows)
    rot270 = turn270(cols)
    # 출력 조건에 맞게 출력
    print(f'#{t}')
    for i in range(N):
        print(f'{rot90[i]} {rot180[i]} {rot270[i]}')