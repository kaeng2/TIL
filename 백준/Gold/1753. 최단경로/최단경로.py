import sys
input = sys.stdin.readline
import heapq

'''
다익스트라 알고리즘
'''

# 입력
V, E = map(int, input().split())            # 노드 개수, 간선 개수
K = int(input())                            # 시작 노드
link = [[] for _ in range(V+1)]             # 간선 정보
for _ in range(E):
    u, v, w = map(int, input().split())
    link[u] += [(w, v)]                     # link[i] = [(가중치 w, 연결 노드 v), (w, v), ...]
# 최단 거리 계산
d_min = [float("inf")] * (V+1)              # d_min[i] = 출발 노드에서 i번 노드까지 최단 거리
Q = [(0, K)]                                # 출발점 최단 거리는 0으로 설정
d_min[K] = 0
while Q:
    d, now = heapq.heappop(Q)               # now까지의 최단 거리, 현재 노드
    if d > d_min[now]:                      # 최신 정보가 아니면 버린다
        continue
    for w, adj in link[now]:                # now와 연결된 노드 중에
        if d + w < d_min[adj]:                  # 지금까지 계산된 해당 노드까지의 최단 거리보다 now를 거쳐서 가는 거리가 짧다면
            d_min[adj] = d + w                      # d_min[adj] 최소값으로 갱신
            heapq.heappush(Q, (d_min[adj], adj))    # 해당 노드 enqueue
# 출력
for ans in d_min[1:]:
    if ans == float("inf"):
        print("INF")
    else:
        print(ans)