import sys
input = sys.stdin.readline
import heapq

'''
최소 스패닝 트리!

단순히 별자리 만들기 문제의 3차원 버전인 것 같지만.. 시간을 줄이는게 관건인 문제다.

이 문제에서는 일반적인 Kruskal MST 알고리즘에 특정 조건에 맞는 간선만 선택하는 과정을 추가함으로써 고려할 간선의 수를 줄여야한다.
각 축을 기준으로 인접한 두 별 사이의 간선을 제외한 나머지 간선은 고려할 필요가 없기 때문이다. (증명 참고)
따라서 간선들을 heappush하는 과정에서, 각 별의 좌표를 X축으로 정렬하여 i번째 별과 (i+1)번째 별 사이의 터널만 enqueue한다. 
Y축과 Z축 기준으로도 동일하게 진행한다.
이후에는 일반적인 Kruskal MST 알고리즘대로 진행한다.
'''

def find(x):
    if parent[x] == x:
        return x
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


N = int(input())                                # 행성의 개수
loca = [0] * N                                  # loca[i] = i번째 행성의 (x좌표, y좌표, z좌표, 고유 번호(인덱스))
for i in range(N):
    X, Y, Z = map(int, input().split())
    loca[i] = (X, Y, Z, i)

Q = []
for t in range(3):                      # 각각의 축에 대해
    loca.sort(key=lambda x: x[t])           # loca를 정렬
    for i in range(1, N):                   # 인접한 두 별을 잇는 (비용, 첫번째 별의 고유번호, 두번째 별의 고유번호) enqueue
        heapq.heappush(Q, (loca[i][t] - loca[i-1][t], loca[i-1][-1], loca[i][-1]))

parent = list(range(N))         # parent[i] = i번째 노드의 부모 노드
rank = [1] * N                  # rank[i] = i번째 노드를 루트 노드로 하는 트리의 깊이

ans, E = 0, 0                   # 현재까지 선택된 터널의 총 비용, 개수
while E < N-1:                  # 터널을 N-1개 선택하고 종료
    c, a, b = heapq.heappop(Q)      # 가장 비용이 낮은 터널부터 고려
    if find(a) != find(b):          # 두 별이 아직 연결되지 않았다면
        union(a, b)                     # 연결
        ans += c                        # 총 비용 갱신
        E += 1                          # 선택한 터널 개수 한 개 추가
print(ans)