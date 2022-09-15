import sys
input = sys.stdin.readline
from itertools import chain

'''
k의 사촌 = 부모의 부모(조부모)가 같고 부모는 다른 모든 노드!!

* 변수 준비
i번째 노드의 부모 노드를 기록하는 parent 배열
i번째 노드의 자식 노드들을 기록하는 child 배열
현재 부모의 인덱스를 나타낼 p

* 배열 채우기
첫번째 노드는 루트 노드(부모 0, 레벨 1)로 두고, 두 번째 노드부터 순회하면서

    - 이전 노드와 연속하지 않는다면 (= 이전 노드와 부모가 같지 않다면)
        1. 이전 부모의 자식은 모두 지나간 것이므로 그 다음 부모의 자식이다.
           부모 인덱스 p를 1 올려준다.

    1. i는 현재 부모 p의 자식이다. parent[i] = p
    2. p의 자식 노드가 i인 것과 동일한 뜻이니까 child[p] += [i]
    
    - 혹시 순회하다가 k를 만나면
        - 나중에 활용하기 편하라고 k = k의 인덱스 로 바꾸어 저장해놓는다. (값은 index 함수로 찾아야 되니까 불편)

* 사촌 수 계산하기
두 배열이 모두 채워졌다면, 조부모의 번호를 이용해서 부모의 형제 노드들을 걸러내고, 그 노드들의 자식 노드 개수를 세준다.
'''


while True:
    n, k = map(int, input().split())

    if not n:   # 0 0 들어오면 종료
        break

    nodes = [0] + list(map(int, input().split()))
    
    if n < 5:       # n이 4 이하면 사촌의 수는 항상 0
        print(0)
        continue

    parent = [0] * (n+1)
    child = [[] for _ in range(n+1)]

    p = 0   # 현재 부모의 인덱스
    for i in range(2, n+1):

        if nodes[i] == k:   # k의 인덱스를 기록해 놓자
            k = i

        if nodes[i] - nodes[i-1] != 1:      # 이전 노드와 형제가 아닌 경우
            p += 1                              # 부모의 인덱스를 1 올려준다 (이전 부모의 자식 노드가 모두 찼음)

        parent[i] = p                       # i의 부모(인덱스 기준)는 p
        child[p] += [i]

    grandparent = parent[parent[k]]
    k_cousins = list(chain.from_iterable([child[x] for x in range(1, k) if x != parent[k] and parent[x] == grandparent]))
    print(len(k_cousins))