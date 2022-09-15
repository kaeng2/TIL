import sys
input = sys.stdin.readline

'''
tree + dp 로 풀이했다.
우선 cmp[i] = i번째 직원이 받은 칭찬 지수 인 cmp 배열을 만들고, 입력 받은 정보를 채워주었다.
이 때 같은 사람이 여러번 칭찬을 받을 수 있다는 것에 유의!
그리고 for문으로 직원들을 순회하면서 해당 직원의 칭찬 지수에 직속 상사의 칭찬 지수를 더해준다.
'''

# 입력
n, m = map(int, input().split())                            # 직원 수, 칭찬 횟수
superior = list(map(lambda x: int(x)-1, input().split()))   # superior[i] = i번째 직원의 직속 상사

cmp = [0] * n                                               # cmp[i] = i번째 직원이 받은 칭찬 지수
for _ in range(m):
    i, w = map(int, input().split())        
    cmp[i-1] += w

# 상사가 받은 칭찬 흡수하기
for i in range(1, n):
    cmp[i] += cmp[superior[i]]

# 출력
print(*cmp)