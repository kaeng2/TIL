import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import math


# n까지의 누적 합을 반환하는 함수
def cumulative_sum(n):
    # n이 0인 경우
    if n == 0:
        return 0

    # n = 2**k 인 경우
    if n & (n-1) == 0:
        return square[int(math.log2(n))] + 1

    # n = 2**k - 1인 경우
    if n & (n+1) == 0:
        return square[int(math.log2(n+1))]

    floor_n = 2 ** int(math.log2(n))     # n보다 작은 2**k 중 최대값
    '''
    n까지의 누적합 = ( 1 이상 floor_n 미만까지의 누적합 ) + ( floor_n 이상 n 이하까지의 누적합 )
    
    - 1 이상 floor_n 미만까지의 누적합 = square[k]
    
    - floor_n 이상 n 이하까지의 누적합  = cumulative_sum(n - floor_n) + (n - floor_n + 1)
    '''
    return cumulative_sum(n - floor_n) + (n - floor_n + 1) + square[int(math.log2(floor_n))]


A, B = map(int, input().split())

'''
square[k] = 1 이상 2**k 미만! 까지의 누적합
0부터 이진수로 나타냈을 때, 
2**0의 자리는 0 1 0 1 0 1 0 1 ...
2**1의 자리는 0 0 1 1 0 0 1 1 ...
2**2의 자리는 0 0 0 0 1 1 1 1 ...
2**k의 자리는 0이 2**k번, 1이 2**k번씩 반복된다.

따라서 2**(k+1) 미만의 수를 모두 이진수로 나타냈을 때, 모든 자릿수에서 0과 1이 절반씩 나오게 된다.
2**(k+1) 미만의 수에서는 2**0의 자리부터 2**k의 자리까지 존재하므로,
square[k+1] = ( 각 자릿수에서의 1의 개수 ) * ( 자릿수의 개수 ) 
            = ( 2**(k+1) // 2 ) * ( k+1 )
            = ( 2**k ) * ( k+1 )
'''
square = [0] + [k * 2**(k-1) for k in range(1, int(math.log2(B))+2)]
print(cumulative_sum(B) - cumulative_sum(A-1))