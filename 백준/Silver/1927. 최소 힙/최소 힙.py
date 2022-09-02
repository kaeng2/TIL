import sys
input = sys.stdin.readline
import heapq


N = int(input())
Q = []
for _ in range(N):
    x = int(input())
    if not x:                           # 입력이 0인 경우
        if Q:
            print(heapq.heappop(Q))
        else:                               # Q가 비어있는 경우
            print(0)
    else:                               # 입력이 자연수인 경우
        heapq.heappush(Q, x)