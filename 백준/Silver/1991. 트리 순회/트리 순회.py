import sys
input = sys.stdin.readline

# 전위 순회
def preorder(v):
    global pre_od
    if 0 <= v:
        pre_od += chr(v+65)
        preorder(child[0][v])
        preorder(child[1][v])

# 중위 순회
def inorder(v):
    global in_od
    if 0 <= v:
        inorder(child[0][v])
        in_od += chr(v+65)
        inorder(child[1][v])

# 후위 순회
def postorder(v):
    global post_od
    if 0 <= v:
        postorder(child[0][v])
        postorder(child[1][v])
        post_od += chr(v+65)


# 입력
N = int(input())
child = [[0] * N for _ in range(2)]        # child[i][j] = j의 i번째 자식 노드
for _ in range(N):
    p, ch_l, ch_r = map(lambda x: ord(x)-65, input().split())    # 'A'는 0, 'B'는 1, ..., '.'은 -19로 입력 받음
    child[0][p] = ch_l
    child[1][p] = ch_r

# 순회 결과 저장
pre_od, in_od, post_od = "", "", ""
preorder(0)
inorder(0)
postorder(0)

# 출력
print(pre_od)
print(in_od)
print(post_od)