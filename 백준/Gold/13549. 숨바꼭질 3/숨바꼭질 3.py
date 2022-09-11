import sys
sys.stdin.readline
from collections import deque

# 최단 시간을 반환하는 함수
def bfs():
    if N >= K:              # 수빈이가 동생보다 앞에 있으면 한 칸씩 뒤로 움직이는 방법 밖에 없다.
        return N - K
    
    visited = dict()        # 방문 딕셔너리
    visited[N] = 1          # 출발점 방문 처리
    Q = deque([N])          # 출발점 enqueue
    
    while Q:
        now = Q.popleft()                                       # 현재 좌표
        
        teleport = now * 2                                      # 순간이동 시 좌표
        if teleport == K:                                       # 목적지에 도착하면 걸린 시간 반환
            return visited[now]-1
        if teleport <= 100000 and not visited.get(teleport):    # 목적지가 아닌 미방문 지점이라면
            visited[teleport] = visited[now]                        # 방문 처리
            Q.appendleft(teleport)                                  # Q의 맨 앞에 enqueue
        
        for nxt in [now-1, now+1]:                              # 그 외 이동 가능한 좌표에 대해서
            if nxt == K:                                            # 목적지에 도착하면 걸린 시간 반환
                return visited[now]
            if 0 <= nxt <= 100000 and not visited.get(nxt):         # 목적지가 아닌 미방문 지점이라면
                visited[nxt] = visited[now] + 1                         # 방문 처리
                Q.append(nxt)                                           # enqueue


N, K = map(int, input().split())    # 입력
print(bfs())                        # 계산 및 출력