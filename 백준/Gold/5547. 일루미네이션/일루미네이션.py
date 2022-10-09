import sys
input = sys.stdin.readline
from collections import deque

'''
1. 배치도를 입력 받을 때, 가장 자리에 2을 덧대준다.
2. 가장 자리의 좌표를 모두 Q에 넣어준다.
3. BFS를 실행하면서 
    1. 빈 공간을 만나면 값을 2로 바꿔주고 좌표를 Q에 넣는다.
    2. 건물을 만나면 deco에 1을 더해준다.
'''


W, H = map(int, input().split())
arr = [[2] * (W+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(H)] + [[2] * (W+2)]

adj_odd = [(0, -1), (1, -1), (-1, 0), (1, 0), (0, 1), (1, 1)]       # y 좌표가 홀수일 때 인접 좌표
adj_even = [(-1, -1), (0, -1), (-1, 0), (1, 0), (-1, 1), (0, 1)]    # y 좌표가 짝수일 때 인접 좌표
adj = [adj_even, adj_odd]

Q = deque([(w, h) for w in range(W+2) for h in [0, H+1]] + [(w, h) for w in [0, W+1] for h in range(1, H+1)])
deco = 0
while Q:
    x, y = Q.popleft()
    for dx, dy in adj[y % 2]:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= W+1 and 1 <= ny <= H:
            if not arr[ny][nx]:
                arr[ny][nx] = 2
                Q.append((nx, ny))
            elif arr[ny][nx] == 1:
                deco += 1
print(deco)