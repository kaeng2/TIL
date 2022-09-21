import sys
input = sys.stdin.readline

'''
이진 탐색 + 투 포인터

두 개의 용액을 고르는 '용액' 문제의 심화 버전.
for문을 통해 첫 용액을 고르고 첫 용액보다 큰 범위에서 나머지 두 용액을 골랐다.
나머지 두 용액은 '용액' 문제 에서와 동일하게 투 포인터를 이용해서 골랐다.
'''


def choose_3():
    mn = (3 * 10**9, 10**9, 10**9, 10**9)
    for i in range(N-2):        # 첫번째 용액은 i번째 용액.
        s, e = i+1, N-1         # 두번째 용액은 s번째, 세번째 용액은 e번째 용액
        while s < e:
            mix = solutions[i] + solutions[s] + solutions[e]
            mn = min(mn, (abs(mix), solutions[i], solutions[s], solutions[e]))      # 최소값 갱신

            if mix > 0:         # 혼합 용액의 특성값이 0보다 크면
                e -= 1              # 끝 포인터를 작은 쪽으로 당기기
            elif mix < 0:       # 0보다 작으면
                s += 1              # 시작 포인터를 큰 쪽으로 밀기
            else:               # 정확히 0이면
                return mn[1:]       # 종료
    return mn[1:]


N = int(input())                                            # 용액의 개수
solutions = list(map(int, input().split()))                 # 각 용액의 특성값
solutions.sort()
ans = choose_3()
print(*ans)