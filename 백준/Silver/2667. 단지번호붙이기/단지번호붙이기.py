from collections import deque, Counter


# 한 단지 내에 번호 K를 표시해주는 함수
def bfs(I, J, K):
    Q.append([I, J])
    visited[I][J] = K
    while Q:
        i, j = Q.popleft()
        for d in range(4):                                      # 상하좌우 중 이동할 수 있는 칸에
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and town[ni][nj]:
                town[ni][nj] = 0                                    # 단지 정보를 지우고
                visited[ni][nj] = K                                 # 방문 배열에 K 표시
                Q.append([ni, nj])
    return


# 입력
N = int(input())                                        # 마을 크기
town = [list(map(int, input())) for _ in range(N)]      # 마을 내 단지 정보
visited = [[0] * N for _ in range(N)]
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
Q = deque()
# 단지 탐색
k = 1
for x in range(N):                  # 모든 좌표를 순회하면서
    for y in range(N):
        if town[x][y]:                  # 단지가 나타나면
            bfs(x, y, k)                    # 해당 단지를 지우면서 방문 배열에 K 표시
            k += 1                          # 다음 단지는 K+1을 표시하여 이전 단지와 구분
cnt = Counter()
# 정답 계산
for row in visited:                 # 단지 별로 집의 개수 세기     
    cnt += Counter(row)
del cnt[0]                          # 0은 단지가 아니므로 삭제
ans = sorted(cnt.values())          # 오름차순 정렬
print(len(ans), *ans, sep='\n')     # 단지 개수, 단지 별 집의 개수 출력