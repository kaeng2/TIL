import sys
input = sys.stdin.readline


def find(x):
    if root[x] == x:
        return x

    # ------------------- find 함수 최적화 ------------------- #

    # x의 모든 조상 노드들의 root 배열 값을 최상위 루트 노드로 채워줌
    root[x] = find(root[x])
    return root[x]


def union(x, y):
    x = find(x)     # x의 루트 노드
    y = find(y)     # y의 루트 노드

    if x == y:      # 이미 같은 집합인 경우
        return

    # ------------------- union 함수 최적화 ------------------- #

    # 깊이가 더 짧은 트리를 밑으로 붙여준다 (짧으면 시간이 덜 걸리니까)
    if rank[x] < rank[y]:
        root[x] = y             # 더 짧은 트리의 루트 x를 더 긴 트리의 루트 y의 자식 노드로 넣어버린다
    else:
        root[y] = x             # 위와 반대
        if rank[x] == rank[y]:
            rank[x] += 1        # 두 트리의 깊이가 동일하다면 x의 rank는 1 늘어난다.


n, m = map(int, input().split())    # 노드의 개수, 연산의 개수
root = list(range(n+1))             # root[i] = i번 노드의 부모 노드
rank = [1] * (n+1)                  # rank[i] = i번 노드를 루트로 하는 트리의 깊이

for _ in range(m):
    cal, a, b = map(int, input().split())

    # 합집합 연산
    if cal == 0:
        union(a, b)

    # 두 원소가 같은 집합에 포함되어 있는지 확인하는 연산
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')