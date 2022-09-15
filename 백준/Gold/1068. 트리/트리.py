import sys
input = sys.stdin.readline
from collections import deque


N = int(input())                            # 노드의 개수
parent = list(map(int, input().split()))    # parent[i] = i번 노드의 부모 노드
child = [[] for _ in range(N)]              # child[i] = i번 노드의 자식 노드 목록
for i in range(N):
    if parent[i] != -1:
        child[parent[i]] += [i]

D = int(input())            # 삭제할 노드
nodes = set(range(N))       # 전체 노드 목록
Q = deque([D])              # 삭제할 노드부터 탐색
while Q:                    # Q가 빌 때까지
    d = Q.popleft()             # d = 현재 노드
    nodes.discard(d)            # 노드 삭제
    parent[d] = -1              # p의 부모는 없는 것으로 설정
    for c in child[d]:          # p의 자식 노드 c에 대해
        Q.append(c)                 # enqueue

'''
리프 노드 = 삭제된 노드를 제외한 노드 중에 다른 노드의 부모 노드가 아닌 노드
'''
print(len(nodes - set(parent)))