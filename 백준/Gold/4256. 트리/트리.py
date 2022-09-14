import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 이진 탐색 트리의 전위, 중위 순회 결과를 후위 순회 결과로 변환하여 출력하는 함수
def to_post(s1, e1, s2):      # 전위 순회 결과의 시작 인덱스, 끝 인덱스, 중위 순회 결과의 시작 인덱스
    # 종료 조건
    if s1 > e1:
        return
    
    root = pre_od[s1]           # 전위 순회 함수는 루트가 가장 먼저
    rt_idx = in_od.index(root)  # 중위 순회 결과에서 루트의 위치
    sub_l = rt_idx - s2         # 왼쪽 서브 트리에 속하는 노드의 개수 = 중위 순회 결과에서 루트 왼쪽에 있는 노드의 개수
    
    # 후위 순회 출력
    to_post(s1+1, s1+sub_l, s2)         # 왼쪽 서브 트리 탐색
    to_post(s1+sub_l+1, e1, rt_idx+1)   # 오른쪽 서브 트리 탐색
    print(root, end=' ')


for t in range(int(input())):
    n = int(input())                            # 노드의 개수
    pre_od = list(map(int, input().split()))    # 전위 순회 결과
    in_od = list(map(int, input().split()))     # 중위 순회 결과
    to_post(0, n-1, 0)
    print()