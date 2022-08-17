# 입력
N, M = map(int, input().split())
rows = [list(input()) for _ in range(N)]
# 열 생성
cols = list(zip(*rows))
r, c = 0, 0
# 경비가 없는 행 개수
for row in rows:
    if 'X' not in row:
        r += 1
# 경비가 없는 열 개수
for col in cols:
    if 'X' not in col:
        c += 1
# 둘 중 최대값 출력
print(max(r, c))