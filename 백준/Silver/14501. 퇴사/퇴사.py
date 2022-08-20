# 상담 가능한 날 수
N = int(input())
# info[i] = i일에 잡힌 상담의 [상담 기간, 수익]
info = [list(map(int, input().split())) for _ in range(N)] + [[0, 0]]
# mx[i] = 퇴사 전 i일부터 퇴사할 때까지 얻을 수 있는 최대 이익
mx = [0] * (N+1)
# 뒤에서부터 순회
info.reverse()
for i in range(1, N+1):
    free = i - info[i][0]   # 이번 상담이 끝나면 info[free]에 잡힌 상담부터 다시 시작 가능
    # 이번 상담이 진행 가능한 경우
    if free >= 0:
        # 이번 상담을 진행할 경우: 이번 상담 수익 + 이번 상담이 모두 끝난 후부터의 최대 수익
        # 이번 상담을 안 할 경우: 퇴사 전 i-1일까지의 최대 수익
        # 두 경우 중 최대값 = 퇴사 전 i일부터 퇴사할 때까지 얻을 수 있는 최대 이익
        mx[i] = max(info[i][1] + mx[free], mx[i-1])
    else:
        # 이번 상담을 아예 못하는 경우 최대값 = 퇴사 전 i-1일까지의 최대 이익
        mx[i] = mx[i-1]
# 퇴사 전 N일 ~ 퇴사 동안의 최대 이익 출력
print(mx[N])