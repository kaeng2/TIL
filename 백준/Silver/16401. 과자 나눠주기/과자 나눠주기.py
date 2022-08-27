import sys
input = sys.stdin.readline

# 입력
M, N = map(int, input().split())
snack = list(map(int, input().split()))
# 이진 탐색
s, e = 1, max(snack)
record = []
while s <= e:
    mid = (s+e)//2
    piece = 0               # 조각 개수
    for x in snack:
        piece += x // mid
    if piece >= M:           # 너무 짧게 잘라서 조각 수가 많아진 경우
        s = mid + 1             # 더 길게 자를 수 있는 경우를 계속 탐색
        record += [mid]         # 이 때의 조각 길이 기록
    else:                   # 너무 길게 잘라서 조각 수가 부족한 경우
        e = mid - 1

# 출력
print(max(record, default=0))       # record가 비었다면 0 출력