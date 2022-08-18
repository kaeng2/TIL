# 테스트 케이스 개수
T = int(input())
# 각 테스트 케이스마다
for t in range(1, T+1):
    # 학생 수, 비교 횟수
    N, M = int(input()), int(input())
    # 인접 행렬
    link = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        link[s][e] = 1
    # 각 학생마다 자기보다 큰 학생을 모두 표시해주기
    for i in range(1, N+1):
        # 방문 체크
        visited = [0] * (N+1)
        while True:
            # 현재 학생 기준으로 더 크고, 아직 조사하지 않은 학생 번호 리스트
            search = [x for x in range(1, N+1) if link[i][x] and not visited[x]]
            if search:
                # 순차적으로 조사하기
                for j in search:
                    visited[j] = 1  # 방문 처리
                    # 지금 조사하는 학생보다 또 더 큰 학생이 있다면
                    # 현재 기준 학생의 인접 행렬에 정보를 갱신해줌
                    for k in [y for y in range(1, N+1) if link[j][y] and not visited[y]]:
                        link[i][k] = 1
            # 조사할 학생이 없다면 종료
            else:
                break
    # 자기보다 더 큰 학생 + 더 작은 학생 = (자기를 제외한 모든 학생) 이면 cnt를 1 올려줌
    cols = list(zip(*link))
    cnt = 0
    for i in range(1, N+1):
        if link[i].count(1) + cols[i].count(1) == N-1:
            cnt += 1
    # 출력
    print(f'#{t} {cnt}')