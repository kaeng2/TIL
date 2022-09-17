import sys
input = sys.stdin.readline
from itertools import chain
import heapq

'''
최소 스패닝 트리!

정점의 개수도 많지 않고, 이차원 배열로 입력 받은 간선을 정렬하는 게 까다로울 것 같아서 Prim 알고리즘으로 풀이했다.

이 문제에서 신경 써서 챙겨야 하는 포인트는
    1. 간선 정보가 문자열로 구성된 이차원 배열 형태로 주어진다는 점
        - ord() 함수를 이용해 숫자로 변환
        - 배열의 인덱스를 정점 번호로 이용
        - 배열[i][j]와 배열[j][i]는 동일하게 i번 컴퓨터와 j번 컴퓨터를 연결하는 데 필요한 랜선 길이이므로, 두 값을 비교하여 통일해준다.
    2. 정답 = 기부할 수 있는 최대 랜선 길이 = 전체 랜선 길이 - 필요한 최소 랜선 길이
'''

# 입력
N = int(input())                                        # 컴퓨터의 개수
# 해당 글자가 대문자일 경우, 소문자일 경우, 0일 경우를 나누어 정수형으로 변환해준다
length = [list(map(lambda x: ord(x) - x.islower() * 96 - x.isupper() * 38 - x.isdigit() * 48, input().rstrip())) for _ in range(N)]
ans = sum(chain(*length))                               # 기부할 수 있는 최대 랜선 길이는 전체 랜선의 총 길이로 초기화 해둔다.

for x in range(N):                                  # length를 순회하면서
    for y in range(N):
        if length[x][y] * length[y][x]:             # length[x][y]와 length[y][x]가 둘 다 0이 아니라면
            mn = min(length[x][y], length[y][x])        
            length[x][y], length[y][x] = mn, mn         # x와 y를 연결하는데 필요한 랜선의 길이는 둘 중의 최소값이다.
        else:                                       # length[x][y]와 length[y][x] 중 적어도 하나는 0이라면
            mx = max(length[x][y], length[y][x])
            length[x][y], length[y][x] = mx, mx         # x와 y를 연결하는데 필요한 랜선의 길이는 둘 중의 최대값이다.

# 탐색
visited = [0] * N               # 방문 배열
dist = [53] * N                 # dist[i] = i번 컴퓨터로 들어오는 랜선의 최소 길이

Q = [(0, 0)]
heapq.heapify(Q)
while Q:                        # Q가 비면 종료
    lan, i = heapq.heappop(Q)       # 가장 길이가 짧은 랜선부터 탐색. (랜선 길이, 시작점) 
    if visited[i]:                      # 이미 연결한 컴퓨터면 pass
        continue
    visited[i] = 1                  # 방문 처리
    ans -= lan                      # 이 랜선은 사용했으므로 기부할 수 있는 최대 랜선 길이에서 빼준다.
    for j in range(N):              # i번 컴퓨터랑 연결할 수 있는 컴퓨터 중 필요한 랜선 길이가 지금까지의 최소값 보다 짧은 것은 
        if not visited[j] and dist[j] > length[i][j] > 0:
            heapq.heappush(Q, (length[i][j], j))    # enqueue
            dist[j] = length[i][j]                  # 최소 길이 공식

# 출력
if sum(visited) == N:   # 모든 컴퓨터를 다 연결한 경우
    print(ans)
else:                   # 모든 컴퓨터가 다 연결되지는 않은 경우
    print(-1)