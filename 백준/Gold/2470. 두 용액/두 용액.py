import sys
input = sys.stdin.readline


'''
투 포인터!
시작 포인터와 끝 포인터를 양 끝단에 두고 시작한다.
혼합 용액의 특성값과 0을 비교한 결과에 따라 각 포인터를 가운데 방향으로 이동시킨다.
'''
N = int(input())
solutions = sorted(list(map(int, input().split())))         # 정렬하여 저장
s, e = 0, N-1                                               # 양 끝의 두 용액부터 검사
ans = (2000000001, s, e)
while s < e:                                                # s == e를 만족하면 종료
    mix = solutions[s] + solutions[e]                           # 혼합 용액의 특성값
    ans = min(ans, (abs(mix), solutions[s], solutions[e]))      # 특성값이 0에 더 가까운 두 용액으로 정답 갱신
    if mix < 0:                                                 # 0보다 작으면
        s += 1                                                      # 시작 포인터 옮기기
    elif mix > 0:                                               # 0보다 크면
        e -= 1                                                      # 끝 포인터 옮기기
    else:                                                       # 특성값이 0이면
        break                                                       # 종료
print(*ans[1:])