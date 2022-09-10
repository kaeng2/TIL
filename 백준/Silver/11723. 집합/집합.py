import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'all':
        S = set(range(1, 21))
    elif cmd[0] == 'empty':
        S.clear()
    else:
        x = int(cmd[1])
        if cmd[0] == 'add':
            S.add(x)
        elif cmd[0] == 'remove':
            S.discard(x)
        elif cmd[0] == 'check':
            print(int(x in S))
        elif cmd[0] == 'toggle':
            S = S ^ set([x])