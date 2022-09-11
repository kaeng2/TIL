import sys
input = sys.stdin.readline
from collections import deque

'''
최단 경로의 수도 계산해야 하기 때문에 이동할 수 있는 위치가 중복되더라도 버리지 말고 Q에 넣어줘야 한다.
따라서 enqueue할 때는 방문 처리를 하지 않고, pop할 때 방문 처리를 해주는게 핵심이다.
또한 enqueue할 때 좌표와 함께 해당 좌표까지 걸린 시간을 튜플로 묶어서 enqueue한다.
해당 좌표까지 걸린 시간은 이전 좌표까지 걸린 시간에 1씩 더해서 업데이트 해준다.
목적지에 최초로 도착했을 때 걸린 시간을 저장해두고, 
이후에 목적지에 도착할 때마다 걸린 시간을 이 값과 비교해서 최단 경로일 경우에만 cnt를 1 올려준다.
'''


N, K = map(int, input().split())    # 수빈이의 위치, 동생의 위치
visited = [0] * 100001              # 방문 배열
Q = deque([(N, 1)])                 # (출발점, 소요 시간 초기값) enqueue
visited[N] = 1                      # 출발점 방문 처리
min_time, cnt = 0, 1                # 최소 시간, 최단 경로의 수 (적어도 1개는 존재)
# bfs 탐색
while Q:                                    # Q가 빌 때까지
    now, t = Q.popleft()                        # 현재 좌표, 현재까지 걸린 시간
    visited[now] = 1                            # 현재 좌표 방문 처리!!
    for d in [-1, 1, now]:                      # 이동 가능한 좌표 중 미방문한 좌표에 대해
        nxt = now + d
        if 0 <= nxt < 100001 and not visited[nxt]:
            if nxt == K:                            # 목적지라면 (최초 도착)
                min_time = t                            # 방문 배열에 걸린 시간 기록
                visited[nxt] = 1                        # 방문 처리하고 enqueue는 안함
            else:                                   # 목적지가 아닌 경우
                Q.append((nxt, t + 1))                  # (좌표, 시간) enqueue
        elif nxt == K and t == min_time:        # 목적지에 또! 방문한 경우
            cnt += 1                                # 걸린 시간이 최소값과 같다면 cnt +1
# 출력
print(min_time)   # 최소 시간
print(cnt)        # 최단 경로의 수