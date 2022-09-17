import sys
input = sys.stdin.readline
import heapq


'''
최소 스패닝 트리!

Kruskal 알고리즘의 시간 복잡도 = O( 간선 수 * log2(간선 수) )
Prim 알고리즘의 시간 복잡도 = O( 노드 수 ** 2 )

노드 개수는 최대 10,000개이고 간선 개수는 최대 100,000개라서
간선 선택을 기반으로 하는 Kruskal 알고리즘으로 풀이했다.
'''


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])     # x의 조상 노드들의 parent 값을 모두 루트 노드로 수정
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    # 이미 같은 집합이면 아무 것도 안함
    if x == y:
        return
    # 트리의 깊이가 더 작은 쪽이 밑으로 흡수됨
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        # 트리의 깊이가 동일한 경우
        if rank[x] == rank[y]:
            rank[x] += 1


# 입력
V, E = map(int, input().split())            # 노드 개수, 간선 개수
edge = []                                   # edge[i] = i번째 간선의 (비용, 출발점, 도착점)
for _ in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(edge, (C, A-1, B-1))

rank = [1] * V                              # rank[i] = i를 루트로 하는 트리의 깊이
parent = list(range(V))                     # parent[i] = i번째 노드의 부모

# 간선 선택하기
ans = 0                                     # 현재까지 선택된 간선의 총 비용
e = 0                                       # 현재까지 선택된 간선 개수
while e < V-1:                              # 간선을 V-1개 선택하면 종료
    c, a, b = heapq.heappop(edge)           # 비용이 낮은 순서대로 고려
    if find(a) == find(b):                  # 두 노드가 이미 연결돼 있으면 버린다.
        continue
    union(a, b)                             # 그게 아니라면 a, b를 연결
    ans += c                                # 총 비용 갱신
    e += 1                                  # 선택된 간선 개수 갱신

print(ans)
