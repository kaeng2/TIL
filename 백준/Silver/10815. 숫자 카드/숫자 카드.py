import sys
input = sys.stdin.readline

# 입력
N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
int_list = list(map(int, input().split()))

def binary_search(number):
    s, e = 0, N-1
    while s <= e:
        m = (s+e) // 2
        if cards[m] > number:
            e = m - 1
        elif cards[m] < number:
            s = m + 1
        else:
            return 1
    return 0

for n in int_list:
    print(binary_search(n), end=" ")