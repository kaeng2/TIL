# 10번 실행
for i in range(10):
	# 테스트 케이스 번호 입력
    n = int(input())
	# rows = [[첫째 행], [둘째 행], ... [100번째 행]]
    rows = [list(map(int, input().split())) for j in range(100)]
	# 후에 index error를 방지하기 위해 각 행의 양 옆에 0 하나씩 붙여주자
    rows = [[0] + row + [0] for row in rows]
    # 첫 행 중 1 값들의 인덱스 모음
    idxs = [x[0] for x in zip(range(102), rows[0]) if x[1] == 1]
    
    record = []
    for idx in idxs:
        count = 0
        for row in rows:
            # 목표 인덱스의 양 옆이 다 0이면 count만 세주고 다음 행 검사로 넘어가자
            if 1 not in [row[idx-1], row[idx+1]]:
                count += 1
                continue
            # 목표 인덱스의 왼쪽이 1이면
            elif row[idx-1] == 1:
                count += 1
                # 왼쪽에 0이 나올 때까지 계속 목표 인덱스를 낮추면서 count를 올리자
                while row[idx-1] == 1:
                    idx -= 1  
                    count += 1 
            # 마찬가지로 목표 인덱스의 오른쪽이 1이면  
            else:
                count += 1
                # 오른쪽에 0이 나올 때까지 계속 목표 인덱스를 높이면서 count를 높이자
                while row[idx+1] == 1:
                    idx += 1
                    count += 1
        # record = [첫번째 출발점의 count, 두번째 출발점의 count, ...]
        record += [count]
    # count가 가장 작은 출발점 찾기 (처음에 행의 양 끝에 0을 덧대주었으므로 1을 빼줬다)
    answer = idxs[record.index(min(record))]-1
    print(f'#{n} {answer}')

# 10번 실행
for i in range(10):
	# 테스트 케이스 번호 입력
    n = int(input())
	# rows = [[첫째 행], [둘째 행], ... [100번째 행]]
    rows = [list(map(int, input().split())) for j in range(100)]
	# 후에 index error를 방지하기 위해 각 행의 양 옆에 0 하나씩 붙여주자
    rows = [[0] + row + [0] for row in rows]
    # 첫 행 중 1 값들의 인덱스 모음
    idxs = [x[0] for x in zip(range(102), rows[0]) if x[1] == 1]
    
    record = []
    for idx in idxs:
        count = 0
        for row in rows:
            # 인덱스의 양 옆이 다 0이면 다음 행 검사로 넘어가자
            if 1 not in [row[idx-1], row[idx+1]]:
                continue
            # 인덱스의 왼쪽이 1이면
            elif row[idx-1] == 1:
                # 왼쪽에 0이 나올 때까지 계속 인덱스를 낮추고 count는 1씩 더해주자
                while row[idx-1] == 1:
                    idx -= 1 
                    count += 1
            # 마찬가지로 인덱스의 오른쪽이 1이면
            else:
                # 오른쪽에 0이 나올 때까지 계속 인덱스를 높이고 count는 1씩 빼주자
                while row[idx+1] == 1:
                    idx += 1
                    count += 1
        # record = [첫번째 출발점의 count, 두번째 출발점의 count, ...]
        record += [count]
    # count가 가장 작은 출발점 찾기 (처음에 행의 양 끝에 0을 덧대주었으므로 1을 빼줬다)
    answer = idxs[record.index(min(record))]-1
    print(f'#{n} {answer}')