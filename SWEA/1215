# 10번 실행
for i in range(10):
    # 회문의 길이
    n = int(input())
    # rows = [[첫째 행], [둘째 행], [셋째 행], ...]
    rows = [list(input()) for j in range(8)]
    count = 0
    
    for c in range(8):
        # 각 행의 c번째 요소를 묶어서 열을 만들자
        col = [row[c] for row in rows]
        # idx = 단어 시작점의 위치
        for idx in range(9-n):
            # is_pal = [c번째 행의 idx번째 요소에서 시작하는 n 길이의 단어, c번째 열의 idx번째 요소에서 시작하는 n 길이의 단어]
            is_pal = [rows[c][idx:idx+n], col[idx:idx+n]]
            # 각 단어가 회문인지 검사하여 맞으면 count에 1을 더해준다
            for word in is_pal:
                if word == word[::-1]:
                    count += 1
    print(f'#{i+1} {count}')
    