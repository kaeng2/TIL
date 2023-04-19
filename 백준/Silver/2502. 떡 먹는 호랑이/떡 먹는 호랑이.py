import sys
input = sys.stdin.readline

D, K = map(int, input().split())
A = [1, 0, 1] + [0] * (D-3)
B = [0, 1, 1] + [0] * (D-3)

for i in range(3, D):
    A[i] = A[i-2] + A[i-1]
    B[i] = A[i-1] + A[i]

a = 1
while True:
    b, b_rest = (K - A[-1] * a) // B[-1], (K - A[-1] * a) % B[-1]
    if b_rest == 0 and a < b:
        print(a, b, sep="\n")
        break
    a += 1