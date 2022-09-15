import sys
input = sys.stdin.readline
from collections import deque

'''
bfs로 탐색하면서 각 노드의 부모 노드를 찾아서 배열에 기록해주었다.
'''

N = int(input())                        # 노드의 개수
link = [[] for _ in range(N+1)]         # link[i] = i번 노드와 연결된 노드 목록
for _ in range(N-1):                
    i, j = map(int, input().split())
    link[i] += [j]
    link[j] += [i]
parent = [0] * (N+1)                    # parent[i] = i번 노드의 부모 노드
Q = deque([1])                          # 루트 노드부터 탐색
while Q:                                # Q가 빌 때까지
    p = Q.popleft()                         # p는 현재 부모 노드
    for c in link[p]:                       # p와 연결된 노드 중에
        if not parent[c]:                       # 부모가 아직 없는 노드 c가 있으면
            parent[c] = p                           # c의 부모는 p
            Q.append(c)                             # c를 enqueue

print(*parent[2:], sep='\n')