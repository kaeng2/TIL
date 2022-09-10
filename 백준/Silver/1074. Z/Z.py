import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


# 특정 칸 (r, c)에 방문하는 순서를 출력하는 함수
def z_search(si, sj, n):            # 해당 영역 좌측 상단 꼭짓점 좌표와 영역의 한 변 길이를 인자로 받음
    global order, ans

    # base case
    if n == 1:                      # 영역 크기가 1*1이 되면
        order += 1                      # 방문 순서 기록
        if (si, sj) == (r, c):          # 해당 칸이 (r, c)라면
            ans = order                     # 정답 변수에 방문 순서 저장 후 출력
            print(ans)
        return

    # 정답을 찾고나면 더 이상 실행하지 않음
    if not ans:
        if si <= r < si + n and sj <= c < sj + n:
            z_search(si, sj, n//2)                  # 좌측 상단 영역
            z_search(si, sj + n//2, n//2)           # 우측 상단 영역
            z_search(si + n//2, sj, n//2)           # 좌측 하단 영역
            z_search(si + n//2, sj + n//2, n//2)    # 우측 하단 영역

        else:                   # (r, c)가 해당 영역 내에 없다면
            order += n * n          # 방문 순서만 채워주고 탐색은 안함


N, r, c = map(int, input().split())     # 2**N * 2**N 차원 배열, 행 인덱스, 열 인덱스
n = 2**N                                # 한 변의 길이
order, ans = -1, 0                      # 방문 순서, 정답
z_search(0, 0, n)