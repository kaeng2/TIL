# i보다 더 큰 학생 번호를 Q에 저장해주는 함수
def find_taller(i):
    global Q
    for j in link[i]:
        if j not in Q:
            find_taller(j)
            Q += [j]


# 입력
N, M = map(int, input().split())            # 학생 수, 비교 횟수
# 정보 표시하기
link = [[] for _ in range(N+1)]             # 비교 정보를 2차원 리스트로 표현
arr = [[0]*(N+1) for _ in range(N+1)]       # (N+1)*(N+1) 배열로 표현
for _ in range(M):                          # 비교 정보 입력
    a, b = map(int, input().split())
    link[a] += [b]
    arr[a][b] = 1
# 각 학생마다
for i in range(1, N+1):
    Q = []
    find_taller(i)          # 더 큰 학생을 찾고
    for j in Q:             # arr 배열에 표시해준다
        arr[i][j] = 1

# 자기가 몇 번째인지 알 수 있는 학생의 수 계산하기
cols = list(zip(*arr))                          # arr 배열을 열 기준으로 묶은 것
cnt = 0
'''
해당 학생 번호의 행에는 자기보다 더 큰 학생이 1로 기록되어 있고, 
해당 학생 번호의 열에는 자기보다 더 작은 학생이 1로 기록되어 있다.
'''
for i in range(1, N+1):                         # 자신을 제외한 N-1명의 학생이 자기보다 크거나, 작으면 cnt를 1 높인다
    if sum(arr[i]) + sum(cols[i]) == N-1:
        cnt += 1
# 출력
print(cnt)