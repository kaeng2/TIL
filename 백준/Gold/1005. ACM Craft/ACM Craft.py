import sys
input = sys.stdin.readline
from collections import deque

'''
* 위상정렬 + DP *
'''


for _ in range(int(input())):                               # 테스트 케이스마다
    N, K = map(int, input().split())                            # 건물의 개수, 건설 순서 규칙의 개수
    t = list(map(int, input().split()))                         # t[i] = i번째 건물의 건설 시간

    after = [[] for _ in range(N)]                              # after[i] = i번째 건물이 짓고 나서야 건설할 수 있는 건물 목록
    indgr = [0] * N                                             # indgr[i] = i번째 건물을 짓기 전에 지어야 할 건물 개수

    Q = set(range(N))                                           # 모든 선행 조건이 완료되어 지금 지을 수 있는 건물 목록
    for _ in range(K):
        X, Y = map(lambda x: int(x) - 1, input().split())       # 입력 받은 X, Y에 대해서
        after[X] += [Y]                                             # X를 짓고 나서야 Y를 지을 수 있음
        indgr[Y] += 1                                               # Y를 짓기 전에 지어야 할 건물 개수 1개 추가
        Q.discard(Y)                                            # Y는 당장 지을 수는 없으므로 Q에서 삭제

    W = int(input()) - 1                                        # 목표 건물
    time_until = t[:]                                           # time_until[i] = i번째 건물이 건설 완료 될 때까지 필요한 시간
                                                                    # 초기값은 각 건물의 건설 시간으로 한다.
    Q = deque(Q)
    while Q:
        now = Q.popleft()           # 현재 건설할 건물

        # 종료 조건
        if now == W:                # W를 짓게 되면 W를 건설 완료할 때까지 걸린 시간을 출력하고 종료
            print(time_until[now])
            break

        for nxt in after[now]:
            '''
            now를 짓고 나서야 지을 수 있는 nxt들에 대해 
            nxt 건설 완료까지 걸린 시간 = now 건설 완료까지 걸린 시간 + nxt를 짓는 시간 이다.
            이 값이 기존에 저장된 값보다 더 클 때에만 갱신한다.
            '''
            time_until[nxt] = max(time_until[nxt], time_until[now] + t[nxt])
            indgr[nxt] -= 1         # 선행 조건 하나 완료
            if not indgr[nxt]:      # 모든 선행 조건이 완료 되어 이제 지을 수 있게 됐다면
                Q.append(nxt)           # enqueue