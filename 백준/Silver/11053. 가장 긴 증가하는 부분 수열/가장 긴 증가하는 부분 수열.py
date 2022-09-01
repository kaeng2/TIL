import sys
input = sys.stdin.readline
from itertools import compress


N = int(input())                        # 수열 A의 크기
A = list(map(int, input().split()))     # 수열 A
part = [0] * (N-1) + [1]                # part[i] = A[i:]에서 가장 긴 증가하는 부분 수열의 길이
# part 채우기
for i in range(N-2, -1, -1):                                    # part[N-2] ~ part[0]까지 차례대로 채우기      
    bigger = [1 if A[i] < x else 0 for x in A[i+1:]]                # A[i] 뒤에 있는 숫자에 대해 A[i] 보다 크면 1, 작으면 0
    mx = max(list(compress(part[i+1:], bigger)), default=0)         # bigger 값이 1인 숫자의 part 값 중 최대값
    part[i] = mx + 1                                                # A[i+1:]에서 가장 긴 증가하는 부분 수열의 길이 + 1 (자기 자신 추가)
# 최대값 출력
print(max(part))