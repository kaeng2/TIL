import sys
input = sys.stdin.readline

'''
N자리 이친수는 N-1자리 이친수 뒤에 0을 붙인 수와 N-2자리 이친수 뒤에 01을 붙인 수로 이루어져 있다.
'''
N = int(input())
pinary_num = [0] * (N+1)
pinary_num[1:3] = [1, 1]
for i in range(3, N+1):
    pinary_num[i] = pinary_num[i-1] + pinary_num[i-2]
print(pinary_num[N])