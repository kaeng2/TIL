import sys
input = sys.stdin.readline
import heapq

'''
1. i번 학생이 파티에 갔다 오는 최단 시간 = i번 마을에서 X번 마을로 가는 최단 시간 + X번 마을에서 i번 마을로 돌아가는 최단 시간
2. 다익스트라 알고리즘으로 X번 마을에서 각각의 마을로 돌아가는 최단 시간을 구한다.
3. 다익스트라 알고리즘으로 i번 마을에서 각각의 마을로 가는 최단 시간을 구하고, 그 중 X번 마을로 가는 최단 시간만 뽑아낸다.
4. 2번에서 구한 최단 시간과 3번에서 구한 최단 시간의 합 중 최대값을 출력한다.
'''

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    min_time = [float('inf')] * N
    min_time[start] = 0
    while Q:
        time_until_now, now = heapq.heappop(Q)
        if min_time[now] < time_until_now:
            continue
        for time_to_adj, adj in link[now]:
            if min_time[adj] > min_time[now] + time_to_adj:
                min_time[adj] = min_time[now] + time_to_adj
                heapq.heappush(Q, (min_time[adj], adj))
    return min_time


N, M, X = map(int, input().split())             # 마을(학생)의 수, 도로 개수, 파티가 열리는 마을 번호
X -= 1                                          # 인덱스로 활용할 수 있도록 조정
link = [[] for _ in range(N)]                   # link[i] = i번 마을에서 갈 수 있는 (도시 번호, 소요 시간)
for _ in range(M):
    s, e, t = map(int, input().split())
    link[s-1] += [(t, e-1)]
ans = dijkstra(X)                               # X번 마을에서 각각의 마을로 돌아가는 최단 시간 리스트
for i in range(N):                              # 각 마을에 대해
    if i != X:                                      # X번 마을은 제외하고
        ans[i] += dijkstra(i)[X]                        # X번 마을에서 돌아오는 최단 시간에 X번 마을까지 가는 최단 시간을 더해준다.
print(max(ans))                                 # 최대값 출력