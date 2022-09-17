import sys
input = sys.stdin.readline
import heapq

'''
최소 스패닝 트리!

Kruskal 알고리즘의 시간 복잡도 = O( 간선 수 * log2(간선 수) )
Prim 알고리즘의 시간 복잡도 = O( 노드 수 ** 2 )

Kruskal 알고리즘 쪽이 시간 복잡도 측면에서는 더 나을 것 같았지만
'만약 특정 도시 B를 정복하고 싶다면, B와 도로로 연결된 도시들 중에서 적어도 하나를 정복하고 있어야 한다' 는 조건이 있어서,
특정 노드를 기준으로 연결된 노드만을 enqueue 하는 Prim 알고리즘으로 풀이했다.
'''

# 입력
N, M, t = map(int, input().split())         # 도시 개수, 도로 개수, 증가하는 도로 비용
link = [[] for _ in range(N)]               # link[i] = i번째 도시와 연결된 (비용, 도시 번호) 목록
for _ in range(M):
    A, B, C = map(int, input().split())
    link[A-1] += [(C, B-1)]
    link[B-1] += [(C, A-1)]

visited = [0] * N                                   # 방문 배열
cost = [10001] * N                                  # cost[i] = i번째 노드로 들어오는 최소 비용
ans = (N-2) * (N-1) * t // 2                        # 모든 도시를 정복하는 동안의 추가 비용을 미리 계산해 둠
Q = [(0, 0)]                                        # 0번째 도시부터 정복
heapq.heapify(Q)
while Q:                                            # Q가 비면 종료
    c, now = heapq.heappop(Q)                           # 최소 비용으로 갈 수 있는 도시 선택
    if visited[now]:                                    # 이미 방문한 곳이면 pass
        continue
    visited[now] = 1                                    # 그게 아니라면 방문 처리
    ans += c                                            # 총 비용 증가
    for c, nxt in link[now]:                            # 현재 도시와 연결된 도시 중에
        if not visited[nxt] and cost[nxt] > c:              # 현재까지 나온 비용보다 더 낮은 비용으로 갈 수 있는 미방문 도시가 있다면
            heapq.heappush(Q, (c, nxt))                         # enqueue
            cost[nxt] = c                                       # 최소 비용 갱신
print(ans)