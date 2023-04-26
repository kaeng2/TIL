import sys
input = sys.stdin.readline

# 입력
X = int(input())

def bit_count(n):
    if n == 0:  return 0
    return n % 2 + bit_count(n // 2)

print(bit_count(X))