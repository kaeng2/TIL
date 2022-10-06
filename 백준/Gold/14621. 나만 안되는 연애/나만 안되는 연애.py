import sys
input = sys.stdin.readline
import heapq

'''
최소 스패닝 트리!
Kruskal 알고리즘의 시간 복잡도 = O( 간선 수 * log2(간선 수) )
Prim 알고리즘의 시간 복잡도 = O( 정점 수 ** 2 )
정점 개수는 최대 1,000개이고 간선 개수는 최대 10,000개라서
간선 선택을 기반으로 하는 Kruskal MST 알고리즘으로 풀이했다.
'''


def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


N, M = map(int, input().split())    # 학교의 개수, 도로의 개수
school = [0] + input().split()      # school[i] = i번 학교의 성비

roads = []
for _ in range(M):
    u, v, d = map(int, input().split())
    heapq.heappush(roads, (d, u, v))

parent = list(range(N+1))
rank = [1] * (N+1)

selected = 0                # 선택된 도로 개수
length = 0                  # 선택된 도로의 총 길이
while selected < N-1:       # 도로가 N-1개 선택되면 종료
    if not roads:               # 선택할 수 있는 도로가 없는 경우
        print(-1)
        break
    dist, a, b = heapq.heappop(roads)
    if find(a) != find(b) and school[a] != school[b]:    # 두 학교가 아직 연결되지 않았고, 성비가 반대인 경우에만 연결 
        union(a, b)
        length += dist
        selected += 1
else:
    print(length)