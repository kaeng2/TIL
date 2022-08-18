# 컴퓨터 개수, 연결 노드 개수
N, M = int(input()), int(input())
# 연결 정보
lst = [list(map(int, input().split())) for _ in range(M)]
link = [[] for _ in range(N+1)]
for x, y in lst:
    link[x] += [y]
    link[y] += [x]
# 돌아갈 지점 저장
stack = []
# 방문 여부 기록
visited = [0] * (N+1)
# 출발점 설정
now = 1
visited[now] = 1
# 탐색 시작
while True:
    # 연결 컴퓨터 중에 미방문한 지점이 있으면 현재 지점 push 후 이동 & 방문 처리
    for nxt in link[now]:
        if not visited[nxt]:
            stack.append(now)
            now = nxt
            visited[now] = 1
            break
    # 연결된 컴퓨터가 없거나, 있더라도 이미 모두 방문했을 경우
    else:
        # 가장 최근 저장된 지점으로 돌아간다
        if stack:
            now = stack.pop()
        # 돌아갈 곳도 없다면 종료
        else:
            break
# 출발점을 제외하고 방문한 지점의 개수를 출력
print(sum(visited)-1)