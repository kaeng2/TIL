# 10번 실행
for i in range(10):    
    # 테스트 케이스 번호를 int로 입력 받자
    n = int(input())
		# 각 행을 정수로 이루어진 리스트로 받고, 이걸 100번 반복
    rows = [list(map(int, input().split())) for j in range(100)]
    # 각 행의 합 중에 최대값을 반환
		max_row_sum = max(map(sum, rows))
    
		# 2차원 리스트를 1차원 리스트로 변환
    ls = sum(rows, [])
		# slicing의 step을 이용해 각 열의 합 구하자
    col_sum = [sum(ls[j::100]) for j in range(100)]
    # step을 이용해 두 대각선의 합을 구하자
    diag_sum = [sum(ls[0::101]), sum(ls[99:-1:99])]
    
		# 전체 중에 최대값 반환
    max_sum = max(max_row_sum, max(col_sum), max(diag_sum))
    print(f'#{n} {max_sum}')