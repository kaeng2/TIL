# 사람 수
N = int(input())
# 각 사람이 돈을 인출하는 데 걸리는 시간
P = list(map(int, input().split()))
# P가 짧을수록 앞 순서에 배치하여 총 대기시간 계산
P.sort(reverse=True)
w = 0
for i in range(N):
    w += (i+1) * P[i]
# 출력
print(w)