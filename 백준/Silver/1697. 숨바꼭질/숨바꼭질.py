import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())        # 수빈이의 위치, 동생의 위치
visited = [0] * 100001                  # 방문 배열
# bfs 탐색
visited[N] = 1                          # 출발점 방문 처리
Q = deque([N])                          # 출발점 enqueue
while Q:                                # Q가 빌 때까지 반복
    now = Q.popleft()                       # 현재 위치
    for d in [-1, 1, now]:
        nxt = now + d                           # 이동 가능한 위치
        if 0 <= nxt <= 100000 and not visited[nxt]:  # 미방문 상태라면
            visited[nxt] = visited[now] + 1              # 이전 위치의 방문 값 + 1을 기록
            Q.append(nxt)                                # enqueue
            if nxt == K:                                 # 동생의 위치에 도달했다면
                Q.clear()                                    # Q를 비워서 반복문 종료
print(visited[K]-1)