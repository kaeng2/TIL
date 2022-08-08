# 테스트 케이스 개수
test = int(input())
# 테스트 케이스마다
for t in range(1, test+1):
    # 배열의 크기, 파리채 크기
    N, M = map(int, input().split())
    # rows = [[첫째 행], [둘째 행], ...]
    rows = [list(map(int, input().split())) for _ in range(N)]
    
    max_fly = 0
    
    # 파리채로 칠 수 있는 블럭의 합을 각각 검사할건데
    # 맨 윗줄 쭉 검사하고 그 다음 줄 검사 ~~
    # s는 시작 행의 index (0행부터 시작)
    s = 0
    while s <= N-M:
        for j in range(N-M+1):
            flies = 0
            for i in range(s, s+M):
                flies += sum(rows[i][j:j+M])
                if flies > max_fly:
                    max_fly = flies
        s += 1
    
    print(f'#{t} {max_fly}')

    