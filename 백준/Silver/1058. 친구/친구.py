import sys
input = sys.stdin.readline

# 2-친구를 모두 찾아서 표시해주는 함수
def two_friend():
    for i in range(N):
        for j in range(N):
            if f1[i][j] == 'Y':     # i와 j가 친구라면
                for k in range(N):          # j의 친구 중 k가
                    if i != k and f1[j][k] == 'Y' and f1[i][k] == 'N':      # i가 아니고, i와 직접 친구가 아니라면
                        f2[i][k] = 'Y'                                          # i와 k는 2-친구이다


N = int(input())                            # 사람 수
f1 = [list(input()) for _ in range(N)]      # 친구 정보 입력
f2 = [[0]*N for _ in range(N)]              # 2-친구 정보 입력
two_friend()                                # 2-친구 찾기
# 최대 친구수 찾기
mx = 0
for i in range(N):
    mx = max(mx, f1[i].count('Y') + f2[i].count('Y'))
print(mx)