from collections import deque

T = int(input())
for t in range(T):
    func = input().replace('RR', '')
    n = int(input())
    if n < func.count('D'):
        print('error')
        arr = input()
        continue
    arr = deque(input().lstrip('[').rstrip(']').split(','))
    r = 0
    for p in func:
        if p == 'R':
            r += 1
        else:
            if r % 2:
                arr.pop()
            else:
                arr.popleft()
    if r % 2:
        arr = ','.join(reversed(arr))
    else:
        arr = ','.join(arr)
    print(f'[{arr}]')