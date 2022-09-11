import sys
input = sys.stdin.readline

'''
dp 배열을 별도로 만들지 않고 입력받은 삼각형 배열의 값을 교체하여 사용했다.
갱신 후의 tr[i][j] = 맨 꼭대기부터 i번째 행까지 왔을 때 j번째 열의 값을 선택하는 경우의 최대값 
i행 j열 지점을 선택하는 경우는 두가지로 나눌 수 있다.
    1. i-1행 j-1열 선택 -> i행 j열 선택
    2. i-1행 j열 선택 -> i행 j열 선택
따라서 tr[i] = max(tr[i-1] + tr[i]) + 기존 tr[i] 값이다.
'''


n = int(input())    # 삼각형의 크기
tr = [list(map(int, input().split())) + [0] * (n-i) for i in range(1, n+1)]     # 숫자가 없는 곳은 0으로 채워주었다.
for i in range(1, n):
    tr[i][0] += tr[i-1][0]      # 삼각형의 왼쪽 변을 타고 내려오는 경로
    tr[i][i] += tr[i-1][i-1]    # 삼각형의 오른쪽 변을 타고 내려오는 경로
    for j in range(1, i):
        tr[i][j] += max(tr[i-1][j-1:j+1])   
print(max(tr[n-1])) 