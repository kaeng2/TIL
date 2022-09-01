import sys
input = sys.stdin.readline

'''
2*N 크기의 직사각형을 채우는 방법은 2*(N-1) 크기의 직사각형을 채우는 방법에 2*1 타일을 붙이는 방법과 
2*(N-2) 크기의 직사각형을 채우는 방법에 1*2 타일을 두개 붙이는 방법으로 이루어져 있다.
'''
N = int(input())
tile = [0] * (N+1)
tile[1:3] = [1, 2]
for i in range(3, N+1):
    tile[i] = tile[i-1] + tile[i-2]
print(tile[N] % 10007)