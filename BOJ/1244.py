# 스위치 개수
N = int(input())
switch = list(map(int, input().split()))
# 학생 수
M = int(input())
# students = [(1, 3), (2, 4), ...]
students = [list(map(int, input().split())) for _ in range(M)]

# 학생 차례대로
for stud in students:
    # 남자일 때
    if stud[0] == 1:
        # 받은 번호부터 끝 번호까지 중에 받은 번호의 배수 번호 스위치를 반대로 바꿔준다
        for i in range(stud[1], N+1, stud[1]):
            switch[i-1] = int(bool(switch[i-1]-1))
    # 여자일 때
    else:
        j = 0
        # 현재 위치 기준으로 양 옆으로 j번째 칸끼리 동일하고, 해당 인덱스가 유효하면
        # 걔네 스위치를 반대로 바꿔준다
        while 0 <= stud[1]-1-j and stud[1]-1+j < N and switch[stud[1]-1-j] == switch[stud[1]-1+j]:
            switch[stud[1]-1-j], switch[stud[1]-1+j] = int(bool(switch[stud[1]-1-j]-1)), int(bool(switch[stud[1]-1+j]-1))
            j += 1

# 한 줄에 20개씩 출력한다
for p in range(N//20+1):
    print(*switch[20*p:20*(p+1)])
