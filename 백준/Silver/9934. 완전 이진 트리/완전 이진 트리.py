import sys
input = sys.stdin.readline


# 트리를 중위 순회 하면서 빌딩 번호를 적는 함수
def inorder(v):
    global i
    if v <= N:
        inorder(2*v)                # 왼쪽 자식 노드 탐색
        tree[v] = footprints[i]     # 왼쪽 자식 노드가 없으면 현재 노드에 빌딩 번호 기록
        i += 1                      # 다음 번호 준비
        inorder(2*v+1)              # 오른쪽 자식 노드 탐색


# 입력
K = int(input())    # 트리의 깊이
N = 2**K - 1        # 트리의 노드 개수
footprints = list(map(int, input().split()))    # 중위 순회 결과
# tree 채우기
tree = [0] * (N+1)  
i = 0
inorder(1)
# 출력
for level in range(K):
    for n in range(2**level, 2 * 2**level):     # 각 레벨의 첫번째 노드 번호는 2**레벨, 각 레벨의 노드 개수는 2**레벨.
        print(tree[n], end=' ')
    print()