# 테스트 케이스 개수
T = int(input())
# 각 테스트 케이스마다
for t in range(T):
    # 출발점, 도착점
    x, y = map(int, input().split())
    '''
    이동 횟수를 최소화 하면서 첫 시기에 1광년, 마지막 시기에도 1광년 이동해서 돌아오려면
    1광년, 2광년, 3광년, ..., M광년, M-1광년, M-2광년, ..., 3광년, 2광년, 1광년 처럼
    이동 거리가 1에서 M까지 늘어났다가 다시 1로 줄어드는 형태로 이동 해야한다.
    
    이 때 이동 거리의 총합은 (M-1)*M + M = M**2 이며 이동 횟수는 2*M - 1이다.
    '''
    M = 0
    while (M+1)**2 <= y-x:   # 이동 거리가 출발점과 도착점 사이의 거리를 넘지 않도록 하는 최대 M을 찾는다
        M += 1
    move = 2 * M - 1    # 이동 횟수
    if y-x != M**2:     # 아직 이동할 거리가 남은 경우
        if y-x - M**2 > M:  # 남은 거리가 M을 초과하면 2번의 이동이 추가로 필요하다
            move += 2
        else:               # 남은 거리가 M 이하라면 1번의 추가 이동으로 도착할 수 있다
            move += 1
    print(move)         # 출력