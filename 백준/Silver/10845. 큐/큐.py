import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
Q = deque()
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        Q.append(command[1])
    elif command[0] == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(Q))
    elif command[0] == 'empty':
        print(int(len(Q) == 0))
    elif command[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)