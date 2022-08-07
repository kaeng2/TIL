# 10번 실행
for test in range(10):
    n = input() # 100
    # rows = [[첫째 행], [둘째 행], ...]
    rows = [list(map(int, input().split())) for _ in range(100)]
    # cols = [(첫째 열), (둘째 열), ...]
    cols = list(zip(*rows))
    # 튜플 형태인 cols의 원소를 리스트로 바꿔줬다
    cols = [list(col) for col in cols]
    
    # 교착 상태의 개수
    stuck = 0
    # 각 열마다
    for col in cols:
        # 0을 다 제거해주고
        ls = [elem for elem in col if elem != 0]
        # 남은 숫자는 문자열로 변환 후 공백 없이 합쳐서 하나의 문자열로 만들었다
        # 그 문자열에 들어있는 '12'의 개수를 반환
        count = ''.join(map(str, ls)).count('12')
        stuck += count
    print(f'#{test+1} {stuck}')