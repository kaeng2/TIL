import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 배열 크기
N = int(input())
# 높이 정보
height = [list(map(int, input().split())) for _ in range(N)]
mx, mn = 1, 100     # 최대 높이, 최소 높이
for row in height:
    x, n = max(row), min(row)
    mx, mn = max(mx, x), min(mn, n)
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]   # 이동 방향
mx_cnt = 1  # 안전 영역 최대 개수

# 한 개의 안전 영역 내부 모든 지역에 방문 처리를 해주는 함수
def safe_zone(i, j, r):
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and height[ni][nj] > r and not visited[ni][nj]:
            visited[ni][nj] = 1
            safe_zone(ni, nj, r)

# 비의 양에 따른 안전 영역 개수 계산
for r in range(mn, mx):
    cnt = 0     # 안전 영역 개수
    visited = [[0]*N for _ in range(N)]     # 방문 체크
    for i in range(N):
        for j in range(N):
            if height[i][j] > r and not visited[i][j]:
                visited[i][j] = 1   # 해당 칸 방문 처리
                safe_zone(i, j, r)  # 연결된 지역 모두 방문 처리
                cnt += 1            # 안전 영역 개수 += 1
    mx_cnt = max(mx_cnt, cnt)
# 출력
print(mx_cnt)