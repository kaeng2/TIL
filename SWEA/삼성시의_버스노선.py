# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test + 1):
    # 버스 노선 개수
    N = int(input())
    # path = [[A1, B1], [A2, B2], ..., [AN, BN]]
    path = [list(map(int, input().split())) for _ in range(N)]
    # 체크해야 할 정류장의 개수
    P = int(input())
    # C = [C1, C2, C3, ..., CP]
    C = [int(input()) for _ in range(P)]
    # 버스 개수를 세기 위한 리스트
    # cnt[0]은 1번 정류장의 버스 개수, ..., cnt[max(C)-1]은 max(C)번 정류장의 버스 개수
    cnt = [0] * max(C)
    # 노선의 시작점이 cnt 리스트 안에 있다면 시작 지점 cnt 값에 1을 더해주고,
    # 노선의 끝점이 cnt 리스트 안에 있다면 끝점 바로 다음 지점 cnt 값에 -1을 더해준다.
    for i in path:
        if i[0] <= max(C):
            cnt[i[0]-1] = 1
        if i[1] < max(C):
            cnt[i[1]] = -1
    # C_j번 정류장을 지나는 노선의 개수를 기록할 리스트
    result = []
    # j번 정류장의 버스 개수는 cnt 리스트의 첫 칸부터 j번째 칸까지의 합
    for j in C:
        result += [sum(cnt[:j])]
    print(f'#{t}', *result)
