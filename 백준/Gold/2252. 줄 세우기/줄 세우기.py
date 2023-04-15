import sys
input = sys.stdin.readline
from collections import deque

'''
위상 정렬 : 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

키 순서는 사이클이 없는 방향 그래프이므로 위상 정렬 알고리즘으로 풀이 했다.
1. 연결 배열과 각 노드로 들어오는 노드 개수(진입 차수) 를 기록한 일차원 배열 생성
2. 진입 차수가 0인 모든 노드 enqueue
3. Q가 빌 때까지 반복
    1. Q에서 popleft하고 출력
    2. 현재 노드에서 갈 수 있는 모든 노드의 진입 차수를 하나 줄여줌 (간선 삭제)
    3. 진입 차수가 0이 된 노드가 있다면 enqueue
'''


# 입력 및 변수 선언
N, M = map(int, input().split())    # 학생 수, 비교 횟수
link = [[] for _ in range(N)]       # link[i] = i번 학생보다 뒤에 서야 하는 학생 목록
indegree = [0] * N                  # indegree[i] = i번 학생보다 앞에 서야 하는 학생의 수
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())   # 인덱스로 활용할 수 있도록 1을 빼줬음
    link[a] += [b]          # 연결 배열에 기록
    indegree[b] += 1        # 진입 차수 갱신

# 위상 정렬
Q = deque()
for i in range(N):
    if not indegree[i]:         # 자기보다 앞에 서야할 학생이 없으면 enqueue
        Q.append(i)
while Q:
    now = Q.popleft()
    print(now+1, end=' ')       # now 줄 세우기
    for nxt in link[now]:       # now는 이미 줄을 섰으므로 now보다 나중에 서야할 학생들에 대해
        indegree[nxt] -= 1          # 앞에 한 명 줄었다
        if not indegree[nxt]:       # 앞에 아무도 없으면
            Q.append(nxt)               # 줄 서러 가자~~