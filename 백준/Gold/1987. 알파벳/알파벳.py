import sys
input = sys.stdin.readline

'''
시간초과 때문에 애먹은 문제.
처음엔 dfs 재귀함수로 구현했으나 계속 시간초과가 나왔다.
질문 게시판을 참고해서 set을 이용한 bfs로 풀이했다.
Q에는 (행 번호, 열 번호, 지나온 알파벳, 지나온 칸 수)를 담고, 
다음 칸으로 이동할 때 지나온 알파벳에 이동하는 칸의 알파벳을 추가하고, 칸 수도 하나 늘려준다.
지나온 칸 수를 ans랑 비교하면서 최대값을 갱신해준다.
'''

def bfs():
    ans = 1
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
    Q = set([(0, 0, board[0][0], 1)])
    while Q:
        now_i, now_j, record, cnt = Q.pop()
        ans = max(ans, cnt)
        for d in range(4):
            nxt_i, nxt_j = now_i + di[d], now_j + dj[d]
            if 0 <= nxt_i < R and 0 <= nxt_j < C and board[nxt_i][nxt_j] not in record:
                Q.add((nxt_i, nxt_j, record + board[nxt_i][nxt_j], cnt+1))
    print(ans)

# 입력
R, C = map(int, input().split())
board = [input() for _ in range(R)]

# dfs 탐색 및 출력
bfs()
