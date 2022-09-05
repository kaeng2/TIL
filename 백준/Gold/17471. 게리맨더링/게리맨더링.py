import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

'''
1. itertools.combinations를 이용하여 두 개의 선거구 뽑기
2. 각 선거구가 모두 인접해 있는지 확인
3. 인접하지 않은 선거구가 있다면 skip
4. 두 선거구 모두 인접해 있다면 두 선거구의 인구 차이를 기록
5. 기록된 인구 차이 중 최소값 계산
'''

# 입력 받은 선거구가 모두 연결 되어 있는지 여부를 반환하는 함수
def bfs(team):
    Q = deque([team[0]])        # 출발점 enqueue
    visited = [0] * (N+1)       # 방문 배열
    visited[team[0]] = 1        # 출발점 방문 체크

    while Q:                                    # Q가 빌 때까지
        now = Q.popleft()
        for nxt in link[now]:                       # 현재 구역과 연결된 구역 중에
            if not visited[nxt] and nxt in team:        # 같은 선거구인 미방문 구역이 있다면
                visited[nxt] = 1                            # 해당 구역 방문 체크
                Q.append(nxt)                               # enqueue

    for area in team:                           # 선거구에 속한 지역 중에
        if not visited[area]:                       # 연결되지 않은 지역이 있다면
            return False                                # False 반환
    return True                                 # 모두 연결 되었다면 True 반환


# 지역을 가능한 방법으로 나눈 모든 경우 중 인구 차이의 최솟값을 반환하는 함수
def diff_p():
    record = []                                                     # 각 방법의 인구 차이를 기록할 리스트
    # 구역 1개짜리 선거구와 구역 N-1개짜리 선거구로 나누는 경우
    for i in range(1, N+1):
        team2 = [x for x in range(1, N+1) if x != i]    # N-1개의 구역으로 이루어진 선거구
        if bfs(team2):                                  # 모두 연결되어 있다면
            record += [abs(2 * p[i] - sum(p))]              # record에 인구 차이 기록
    # 그 외의 경우
    for n in range(2, (N//2 + 1)):                                  # n = 선거구 1에 속한 구역 개수
        for team1 in combinations(range(1, N+1), n):                    # 1 ~ N번 구역 중 n개를 뽑는 모든 경우마다
            team2 = [x for x in range(1, N+1) if x not in team1]            # 선거구 2를 결정
            if bfs(team1) and bfs(team2):                                   # 선거구 1과 선거구 2가 각각 연결 되어 있다면
                p_team1 = 0                                                     # p_team1 = 선거구 1의 인구수
                for area in team1:
                    p_team1 += p[area]
                p_team2 = sum(p) - p_team1                                      # p_team2 = 선거구 2의 인구수
                if p_team1 == p_team2:                                          # 두 선거구의 인구가 같은 경우
                    return 0                                                        # 가능한 최소값이므로 0을 반환하고 종료
                record += [abs(p_team1 - p_team2)]                              # record에 두 선거구의 인구 차이 기록
    # 최소값 산출
    if record:                  
        return min(record)      # 기록된 인구 차이 중 최소값 반환
    else:               
        return -1               # 기록된 게 없는 경우는 두 선거구를 나눌 방법이 없는 것이므로 -1 반환


# 입력
N = int(input())                                # 구역의 개수
p = [0] + list(map(int, input().split()))       # p[i] = i번 구역의 인구수
# 인접 구역 리스트 채우기
link = [[] for _ in range(N+1)]                 # link[i] = i번 구역과 인접한 구역 리스트
for i in range(1, N+1):
    adj = list(map(int, input().split()))
    if adj[0]:
        link[i] += adj[1:]
# 계산 및 출력
print(diff_p())