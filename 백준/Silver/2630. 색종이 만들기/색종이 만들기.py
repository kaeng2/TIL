import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import Counter


def dfs(si, sj, n):     # 영역의 좌측 상단 꼭짓점 좌표와 영역 한 변의 길이를 인자로 받는다
    global colors
    v = [(si, sj), (si, sj + n//2), (si + n//2, sj), (si + n//2, sj + n//2)]    # 영역을 4개로 분할했을 때 좌상, 우상, 좌하, 우하 영역의 꼭짓점 좌표

    # base case
    if n == 1:                          # 1*1 영역은 더 이상 분할할 수 없다
        colors += [paper[si][sj]]           # 해당 영역의 색깔을 기록 후 종료
        return

    # 현재 영역이 모두 같은 색으로 칠해져 있는지 확인하기
    color = paper[si][sj]               # 현재 색깔
    for i in range(si, si + n):         # 현재 영역 순회하다가
        for j in range(sj, sj + n):
            if paper[i][j] != color:        # 색깔이 다른 칸이 나오면
                for z in range(4):              # 다시 4개 영역으로 분할하여 각 영역마다 dfs 실행
                    dfs(*v[z], n//2)                # 미리 만들어 둔 영역별 꼭짓점 좌표를 인자로 넣는다
                return
    colors += [color]                   # 모두 같은 색이 칠해져 있다면 현재 색깔 기록 후 종료
    return


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
colors = []                         # 자른 종이의 색깔을 기록할 배열
dfs(0, 0, N)                        
ans = Counter(colors)               # 색깔 별로 종이의 개수 계산
print(ans[0], ans[1], sep='\n')