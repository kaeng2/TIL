import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

'''
집의 좌표가 최대 10억이므로 이진탐색을 이용하여 풀이했다.
'''

N, C = map(int, input().split())                    # 집의 개수, 공유기 개수
houses = sorted([int(input()) for _ in range(N)])   # 집들의 좌표를 오름차순으로 정렬
max_distance = houses[-1] - houses[0]               # 가능한 최대 거리 = 최대 좌표 - 최소 좌표
s, e = 1, max_distance                              # 1 ~ 최대 거리의 범위 내에서 이진 탐색 진행
while s <= e:
    mid = (s+e)//2                      # 가장 인접한 두 공유기 간의 거리를 mid로 설정하여 실험
    v, cnt = houses[0], 1               # 첫번째 집의 좌표, 가장 인접한 두 공유기 간의 거리가 주어졌을 때 설치할 수 있는 공유기 개수
    for i in range(N):                  # 전체 집을 순회하면서
        if houses[i] >= v + mid:            # v에서 mid만큼 떨어진 집이 있다면
            v = houses[i]                       # 그 집을 v로 갱신
            cnt += 1                            # 공유기 개수 +1
    if cnt >= C:                        # 최소 거리가 mid일 때 공유기를 C개 이상 설치할 수 있다면
        ans = mid                           # 일단 ans에 거리를 저장
        s = mid + 1                         # 거리를 늘려본다
    else:                               # 공유기를 C개도 설치하지 못한다면
        e = mid - 1                         # 거리가 너무 넓은 것이므로 거리를 줄여본다
print(ans)