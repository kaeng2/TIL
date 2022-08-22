# 입력
M, N = map(int, input().split())
# 소수 여부를 체크할 리스트 (인덱스가 소수이면 1, 아니면 0)
P = [0, 0] + [1]*(N-1)

# 소수가 아닌 숫자 표시하기
for i in range(2, int(N**0.5)+1):       # 절반의 약수에 대해
    if P[i]:                            # 해당 수가 소수라면 (이미 소수가 아니라고 판정된 i에 대해서는 실행할 필요가 없기 때문)
        for j in range(i*i, N+1, i):    # 그 수의 배수는 전부 소수가 아니다
            P[j] = 0

# 출력
for n in range(M, N+1):
    if P[n]:
        print(n)