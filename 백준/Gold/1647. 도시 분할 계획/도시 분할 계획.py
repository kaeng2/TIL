import sys
input = sys.stdin.readline
import heapq

'''
최소 스패닝 트리!

Kruskal 알고리즘의 시간 복잡도 = O( 간선 수 * log2(간선 수) )
Prim 알고리즘의 시간 복잡도 = O( 정점 수 ** 2 )

정점 개수는 최대 100,000개이고 간선 개수는 최대 1,000,000개라서
간선 선택을 기반으로 하는 Kruskal MST 알고리즘으로 풀이했다.

이 문제는 유지비를 최소로 하면서 마을을 두개로 분할해야 하므로 
보통의 Kruskal MST 알고리즘과 동일하나, 간선을 N-2개 선택하도록 구현해야 한다. 
'''


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


N, M = map(int, input().split())            # 집의 개수, 길의 개수
edge = []                                   # edge[i] = i번째 길의 (비용, 시작점, 도착점)
for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(edge, (C, A-1, B-1))

parent = list(range(N))                     # parent[i] = i번 노드의 부모 노드
rank = [1] * N                              # rank[i] = i번 노드를 루트 노드로 하는 트리의 깊이

E, ans = 0, 0                               # 지금까지 선택된 도로 개수, 지금까지 선택된 도로의 총 유지비
while E < N - 2:                            # 도로를 N-1개 선택하고 종료
    c, a, b = heapq.heappop(edge)               # 유지비가 가장 적은 도로부터 선택할지 말지 생각하자
    if find(a) != find(b):                      # a와 b가 이미 같은 마을이라면 버리자
        union(a, b)                                 # 두 집을 잇고
        ans += c                                    # 총 유지비 갱신
        E += 1                                      # 도로 개수 하나 추가
print(ans)