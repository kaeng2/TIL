# 가로 길이, 세로 길이
N, M = map(int, input().split())
# 가게의 개수
K = int(input())
# 가게 위치
loca = [list(map(int, input().split())) for _ in range(K)]
# 동근이의 위치
dg = list(map(int, input().split()))
# 최단거리의 합
path = 0

# 여기서 '좌표'란 출력에서 주어진 좌표를 의미 (왼쪽 변, 혹은 윗쪽 변에서부터의 거리)

for store in loca:
    # 동근이와 상점이 같은 방향에 있으면 최단 거리는 abs(두 좌표의 차)
    if dg[0] == store[0]:
        path += abs(dg[1] - store[1])
    # 동근이와 가게가 남북으로 마주 보는 경우
    # 세로 길이인 M만큼은 무조건 지나야 하며
    # 가로 방향에서는 동근이와 가게의 좌표의 합, 또는 그 반대방향인 N-동근 좌표 + N-가게 좌표의 합 중 더 작은 것을 고른다
    elif dg[0] + store[0] == 3:
        temp = dg[1] + store[1]
        path += M + temp + 2*(N-temp)*int(temp > N)
    # 동근이와 가게가 동서로 마주 보는 경우
    # 윗 경우와 가로 세로만 반대!
    elif dg[0] + store[0] == 7:
        temp = dg[1] + store[1]
        path += N + temp + 2 * (M - temp) * int(temp > M)
    # 동근이와 가게가 북동 혹은 남서로 이웃한 경우
    elif dg[0] + store[0] == 5:
        # 동근이와 가게 중 방향의 숫자가 더 낮은 순서대로 배열
        temp = [dg, store]
        temp.sort(key=lambda x: x[0])
        # 남서로 이웃한 경우
        # 남쪽에 있는 애 좌표 + ( M - 서쪽에 있는 애 좌표 )
        if temp[0][0] == 1:
            path += N - temp[0][1] + temp[1][1]
        # 북동으로 이웃한 경우
        # ( N - 북쪽에 있는 애 좌표 ) + 동쪽에 있는 애 좌표
        else:
            path += temp[0][1] + M - temp[1][1]
    # 동근이와 가게가 북서 혹은 남동으로 이웃한 경우
    else:
        temp = dg[1] + store[1]
        # 북서로 이웃한 경우
        if dg[0] + store[0] == 4:
            path += temp
        # 남동으로 이웃한 경우
        else:
            path += N + M - temp

print(path)