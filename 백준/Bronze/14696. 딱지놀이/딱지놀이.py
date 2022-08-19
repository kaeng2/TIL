# 총 라운드 수
N = int(input())
# 매 라운드마다
for _ in range(N):
    # 입력
    a, A = input().split(maxsplit=1)
    b, B = input().split(maxsplit=1)
    A, B = A.split(), B.split()
    # 모양 리스트
    shape = ['4', '3', '2', '1']
    # 승부 
    i = 0
    while i < 4:
        A_cnt, B_cnt = A.count(shape[i]), B.count(shape[i])
        if A_cnt == B_cnt:    # 해당 모양 개수가 동일하면 다음 모양으로 넘어간다
            i += 1
            continue
        elif A_cnt > B_cnt:   # 해당 모양이 더 많은 사람이 승자
            result = 'A'
            break
        elif A_cnt < B_cnt:
            result = 'B'
            break
    # 모양을 전부 검사 하는 동안 승부가 안나면 무승부
    else:
        result = 'D'
    # 출력
    print(result)