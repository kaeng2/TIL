# 입력이 10개니까 10번 돌리자
for i in range(10):
		# 전체 길이 받아서 int로 바꾸고
    length = int(input())
		
		# 빌딩 높이 리스트로 바꾸고
    height_ls = list(map(int, input().split()))
	
    view = 0
		
    # 각 빌딩마다
    for building in range(2, length-2):
				# 조망권이 확보된 칸 수 세기
        # 양 옆 두 빌딩 중 최대 높이보다 더 튀어나온 부분이 몇 칸인지 측정하는 방식
        count = height_ls[building] - max(max(height_ls[building-2: building]), max(height_ls[building+1: building+3]))
        # 조망권이 확보된 칸이 있다면 view에 더해주자
        if count > 0:
            view += count
    # 입력번호랑 조망권이 확보된 칸 개수 출력해주면 끝
    print(f'#{i+1} {view}')