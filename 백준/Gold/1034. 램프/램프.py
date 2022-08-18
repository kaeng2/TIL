# 행, 열 개수
N, M = map(int, input().split())
# 스위치 정보
rows = [input() for _ in range(N)]
switch_dict = {}
# 스위치 누를 횟수
K = int(input())
# K가 홀수라면
if K % 2:
    # 0이 K개보다 많으면서 홀수 개인 행 중에 동일한 것끼리 개수를 세준다
    for row in rows:
        z = row.count('0')
        if z % 2 and z <= K:
            switch_dict[row] = switch_dict.get(row, 0) + 1
# K가 짝수라면
else:
    # 0이 K개보다 많으면서 짝수 개인 행 중에 동일한 것끼리 개수를 세준다
    for row in rows:
        z = row.count('0')
        if z % 2 == 0 and z <= K:
            switch_dict[row] = switch_dict.get(row, 0) + 1
# 결과 출력
if switch_dict:
    print(max(switch_dict.values()))
else:
    print(0)