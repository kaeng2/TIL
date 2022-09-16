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
        size[y] += size[x]      # size[y] = 두 트리의 사이즈의 합
    else:
        root[y] = x             # 위와 반대
        size[x] += size[y]      # size[x] = 두 트리의 사이즈의 합
        if rank[x] == rank[y]:
            rank[x] += 1        # 두 트리의 깊이가 동일하다면 x의 rank는 1 늘어난다.


for t in range(int(input())):
    F = int(input())
    root = list(range(2*F))         # root[i] = i번째 노드의 부모 노드
    rank = [1] * (2*F)              # rank[i] = i번째 노드를 루트로 하는 트리의 깊이
    size = [1] * (2*F)              # size[i] = i번째 노드를 루트로 하는 트리에 속한 노드 개수
    user = dict()                   # {유저1 이름: 유저1 인덱스, 유저2 이름: 유저2 인덱스, ...}
    idx = 0
    for _ in range(F):
        A, B = input().split()
        # 새로운 유저라면 딕셔너리에 추가
        if user.get(A, -1) < 0:
            user[A] = idx
            idx += 1
        if user.get(B, -1) < 0:
            user[B] = idx
            idx += 1
        # 친구 네트워크 병합
        union(user[A], user[B])
        # 사이즈 출력
        print(size[find(user[A])])