import sys
input = sys.stdin.readline
from collections import deque

'''
stk에는 추후에 다른 수의 오큰수가 될 가능성이 있는 숫자만 담는다.
수열을 거꾸로(오 -> 왼) 훑으면서 어떤 수 n의 왼쪽에서 n보다 큰 수를 찾았다면, n은 더 이상 오큰수가 될 가능성이 없다.
예를 들어 수열이 [..., 3, 5, 1, 2] 와 같이 주어진 경우, 2는 자기보다 왼쪽에 있는 5를 찾은 시점부터는 어떤 수의 오큰수도 될 수 없다.
'''

N = int(input())                        # 수열의 크기
A = list(map(int, input().split()))     # 수열
stk = deque()                           # stk에는 오큰수가 될 가능성이 있는 숫자만 담는다
NGE = [0] * N                           # NGE[i] = A[i]의 오큰수
NGE[-1] = -1                            # A[N]의 오큰수는 항상 -1이다

for i in range(N-1, 0, -1):             # 수열을 거꾸로 훑으면서
    if A[i-1] < A[i]:                       # 이 경우 A[i]가 A[i-1]의 오큰수가 된다 
        NGE[i-1] = A[i]
        stk.append(A[i])                        # enqueue
    else:                                   # 이 경우에는 stk을 뒤진다
        while stk:
            if A[i-1] < stk[-1]:                    # stk에 가장 최근 저장된 수가 A[i-1]보다 크다면
                NGE[i-1] = stk[-1]                      # 그 수가 오큰수가 된다
                break                                   # 오큰수를 찾았으니 다음 i로 넘어간다
            else:                                   # stk에 가장 최근 저장된 수가 A[i-1]보다 작다면
                stk.pop()                               # 추후에도 오큰수가 될 가능성이 없으므로 pop
        else:                                   # stk을 다 뒤져도 오큰수를 못 찾은 경우
            NGE[i-1] = -1                           # 오큰수는 -1
print(*NGE)