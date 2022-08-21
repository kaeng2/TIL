import sys
input = sys.stdin.readline

# 입력
K, N = map(int, input().split())        # 갖고있는 랜선 개수, 만들어야 할 랜선 개수
L = [int(input()) for _ in range(K)]    # 랜선 길이 리스트
# 가능한 최대 길이
mx_len = sum(L) // N
# 길이를 기록하는 용도
record = []
if mx_len > 1:
    # 이분 탐색
    s, e = 1, mx_len
    while s <= e:
        mid = (s+e) // 2
        piece = sum([x // mid for x in L])  # mid만큼 잘랐을 때 만들 수 있는 조각 개수
        if piece < N:
            e = mid - 1
        else:
            record += [mid]     # 조각의 길이 기록
            s = mid + 1
    print(max(record))
# 최대 길이가 1 이하라면 바로 출력
else:
    print(mx_len)