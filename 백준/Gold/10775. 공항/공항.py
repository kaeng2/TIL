import sys
input = sys.stdin.readline


'''
각 비행기마다 도킹 가능한 최대 번호의 게이트에 도킹시키는 그리디 문제이다.
다만 해당 번호의 게이트가 이미 차 있다면 그보다 1 작은 번호의 게이트를 검사해야 하는데,
이렇게 각 비행기마다 G개의 게이트를 모두 검사하다보면 시간 초과가 나온다.
그래서 union, find 함수를 통한 경로 압축을 이용해서 가능한 최대 번호의 게이트로 바로 이동하도록 구현하는게 관건이었다.

이 문제에서의 parent 배열은 특정 게이트의 차선책을 나타낸다.
i번 게이트가 비어있다면 i번 게이트에 바로 도킹할 수 있으므로 parent[i]는 i이다.
그러나 만약 i번 게이트가 차 있다면 i-1번 게이트에 도킹해야 하므로 parent[i] = i-1이다.
이 때 i-1번 게이트 역시 차 있다면 parent[i]는 그 다음 차선책인 i-2번을 가리키게 된다.
이 과정을 반복하다가 parent[i]가 0이 되었다는 것은 i번 게이트의 차선책이 없다,
즉 i번 이하의 빈 게이트가 더 이상 존재하지 않는다는 것을 의미한다. 
'''


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])     # 경로 압축
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


G = int(input())                # 게이트의 수
P = int(input())                # 비행기의 수
parent = list(range(G+1))       # parent[i] = i번 이하의 빈 게이트의 번호 중 최대값

for i in range(P):              # i번째 (0~P-1) 비행기에 대해서
    g = int(input())                # i번째 비행기가 도킹할 수 있는 게이트 번호 중 최대값
    empty = find(g)                 # g번 이하의 빈 게이트 번호 중 최대값
    if empty == 0:                  # g번 이하의 빈 게이트가 없다면 도킹 실패
        ans = i                         # 도킹 성공한 비행기는 i대
        break                           # 종료
    union(empty-1, empty)           # 최대 번호의 빈 게이트에 도킹 후, 해당 게이트보다 번호가 하나 작은 게이트를 차선책으로 지정해준다.
else:
    ans = P                     # 모든 비행기가 도킹에 성공한 경우
print(ans)