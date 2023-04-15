import sys
input = sys.stdin.readline
import heapq

# 입력
N, M, K, X = map(int, input().split())
link = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    link[A] += [B]
    
min_cost_to = [K+1 for _ in range(N+1)]
min_cost_to[X] = 0
Q = [(0, X)]
while Q:
    cost, now = heapq.heappop(Q)
    
    if min_cost_to[now] < cost:
        continue
    for nxt in link[now]:
        if min_cost_to[nxt] > cost + 1:
            min_cost_to[nxt] = cost + 1
            heapq.heappush(Q, (min_cost_to[nxt], nxt))

ans = list(filter(lambda x: x[1] == K, enumerate(min_cost_to)))
if len(ans) == 0:
    print(-1)
else:
    for idx, cost in ans:
        print(idx)