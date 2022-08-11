# 이진 탐색 성공까지 걸리는 횟수를 반환하는 함수 정의
def bi_find(total, target):
    l, r = 1, total
    cnt = 0
    if total < target:
        return 1000
    while l <= r:
        cnt += 1
        c = int((l + r) / 2)
        if r - l == 1 or target == c:
            return cnt
        elif target < c:
            r = c
        else:
            l = c


# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # 입력
    P, A, B = map(int, input().split())
    # 출력
    a, b = bi_find(P, A), bi_find(P, B)
    if a < b:
        print(f'#{t} A')
    elif a > b:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')