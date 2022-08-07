# 10번 실행
for i in range(10):
		# 테스트 케이스 번호 입력
    n = int(input())
		# rows = [[첫째 행], [둘째 행], ... [100번째 행]]
    rows = [list(map(int, input().split())) for j in range(100)]
		# 후에 index error를 방지하기 위해 각 행의 양 옆에 0 하나씩 붙여주자
    rows = [[0] + row + [0] for row in rows]
    # 도착점에서 출발점으로 거꾸로 올라가기 위해서 행 순서를 반대로 뒤집어주자
		rows.reverse()
		# 도착지점의 index 저장
    goal = rows[0].index(2)
		# 도착지점이 있는 행부터 출발지점이 있는 행부터 차례대로 검사할건데
    for row in rows:
				# 목표 인덱스의 양 옆이 다 0이면 다음 행 검사로 넘어가자
        if 1 not in [row[goal-1], row[goal+1]]:
            continue
				# 목표 인덱스의 왼쪽이 1이면
        elif row[goal-1] == 1:
						# 왼쪽에 0이 나올 때까지 계속 목표 인덱스를 낮추자
            while row[goal-1] == 1:
                goal -= 1   
				# 마찬가지로 목표 인덱스의 오른쪽이 1이면  
        else:
						# 오른쪽에 0이 나올 때까지 계속 목표 인덱스를 높이자
            while row[goal+1] == 1:
                goal += 1
		
		# 처음에 각 행의 양 끝에 0을 붙여줬기 때문에 출발지점의 인덱스는 goal에서 1을 빼줘야한다
    print(f'#{n} {goal-1}')