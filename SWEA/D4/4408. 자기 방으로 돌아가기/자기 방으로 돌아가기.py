# 테스트 케이스 개수
test = int(input())
for t in range(1, test+1):
    # 돌아가야 할 학생 수
    N = int(input())
    # 현재 방 번호, 돌아가야 할 방 번호
    # 1차원 리스트
    idx = []
    for _ in range(N):
        idx += list(map(int, input().split()))
    # 마주 보는 방을 한 세트로 묶고, 첫 번째 세트에 포함된 방는 0번, 두 번째 세트에 포함된 방은 1번, ... 번호를 부여한다
    # 마주 보는 두 방은 둘 중 어디서 출발/도착 하든지 동일한 개념이기 때문
    idx = [(i-1)//2 if i % 2 else (i//2)-1 for i in idx]
    # 방 별로 겹치는 길의 개수
    cnt = [0]*200
    # 학생마다 이동을 하기 위해 지나야 하는 칸의 값을 1 씩 올려준다
    for i in range(0, N*2, 2):
        s, e = min(idx[i], idx[i+1]), max(idx[i], idx[i+1])
        for j in range(s, e+1):
            cnt[j] += 1
    # cnt의 최대값이 모든 학생들이 이동하는 데에 걸리는 최소 시간이다.
    print(f'#{t} {max(cnt)}')