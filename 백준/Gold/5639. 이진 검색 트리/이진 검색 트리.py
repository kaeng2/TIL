import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 이진 탐색 트리의 전위 순회 결과를 후위 순회 결과로 변환하여 출력하는 함수
def bst_pre_to_post(s, e):      # 시작 인덱스와 끝 인덱스를 인자로 받음
    # 종료 조건
    if s > e:                       
        return
    
    root = pre[s]   # 전위 순회에서는 루트부터 시작
    for i, v in enumerate(pre[s+1:], s+1):
        if v > root:
            rr_idx = i      # 현재 루트를 기준으로 오른쪽 서브 트리의 루트 인덱스
            break
    else:
        rr_idx = e + 1      # 오른쪽 서브트리가 존재하지 않는 경우
    
    # 후위 순회 출력
    bst_pre_to_post(s+1, rr_idx-1)  # 왼쪽 서브 트리 탐색
    bst_pre_to_post(rr_idx, e)      # 오른쪽 서브 트리 탐색
    print(root)                     # 양 쪽 서브 트리 탐색이 끝나면 현재 루트 출력


pre = []
while True:
    try:
        n = input()
        pre += [int(n)]
    except:
        break
bst_pre_to_post(0, len(pre)-1)