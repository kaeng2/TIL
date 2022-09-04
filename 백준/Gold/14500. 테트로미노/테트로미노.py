import sys
input = sys.stdin.readline

'''
ㅣ, ㅗ, ㄴ 모양의 폴리노미오는 공통적으로 정사각형 세 개를 나란히 이어 붙인 도형을 포함하고 있다.
이 도형에 추가로 정사각형 한 개를 붙이는데, 그 위치에 따라서 ㅣ, ㅗ, ㄴ 중 하나의 폴리노미오가 된다.
tetro 함수는 이들 중의 최대 숫자 합을 계산한다.
'''
def tetro(rows, N, M):
    global mx
    di, dj = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -2, 2, -1, 0, 1]   # 추가로 붙일 수 있는 사각형의 위치
    for i in range(N):
        for j in range(1, M-1):
            now = sum(rows[i][j-1:j+2])         # 공통적으로 포함하고 있는 도형의 숫자 합
            for d in range(8):
                ni, nj = i + di[d], j + dj[d]   
                if 0 <= ni < N and 0 <= nj < M:
                    mx = max(mx, now + rows[ni][nj])    # ㅣ, ㅗ, ㄴ 중 가장 큰 숫자 합을 저장

'''
mino 함수는 tetro 함수에서 검증하지 못한 나머지 2개 폴리노미오의 숫자 합을 검사한다.
mino 함수 역시 두 개의 폴리노미오가 공통적으로 포함하고 있는 도형을 기준으로,
한 개의 정사각형을 서로 다른 위치에 추가 해보면서 모든 폴리노미오의 숫자 합을 검사한다.
'''
def mino(rows):
    global mx
    di, dj = [0, 0, 2], [0, 2, 0]
    for i in range(N-1):
        for j in range(M-1):
            now = rows[i][j+1] + sum(rows[i+1][j:j+2])
            for d in range(3):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < N and 0 <= nj < M:
                    mx = max(mx, now + rows[ni][nj])


N, M = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(N)]  # 원래의 종이 배열
cols = list(zip(*rows))                                     # 원래의 종이 배열을 90도 회전한 배열
rev_rows = [list(reversed(row)) for row in rows]            # 원래의 종이 배열을 x축 대칭 시킨 배열
mx = 0
tetro(rows, N, M)
tetro(cols, M, N)   # 90도 회전하여 검사
mino(rows)
mino(rev_rows)      # x축 대칭하여 검사
print(mx)