# 단조 증가인지 확인하는 함수 정의
# 계속 10으로 나눠가면서 나머지끼리 비교한다
def is_mono_inc(number):
    nxt = number // 10
    prev = number % 10
    while nxt > 0:
        now = nxt % 10
        if prev < now:
            return 0
        prev = now
        nxt //= 10
    return 1


# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # 정수의 개수
    N = int(input())
    num = list(map(int, input().split()))
    # 최대값을 빠르게 찾기 위해 내림차순 정렬
    num.sort(reverse=True)
    result = []
    for i in range(N-1):
        for j in range(i+1, N):
            # 단조 증가이면 해당 숫자를 반환하고 반복문 종료
            # 고정된 i에 대해 j가 커질 수록 num[i]*num[j]는 작아지기 때문에 더 볼 필요가 없다
            if is_mono_inc(num[i]*num[j]):
                result += [num[i]*num[j]]
                break
    # 결과값이 한 개 이상 있으면 최대값 출력
    if result:
        print(f'#{t} {max(result)}')
    # 없으면 -1 출력
    else:
        print(f'#{t} -1')