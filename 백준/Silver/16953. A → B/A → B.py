import sys
input = sys.stdin.readline
from collections import deque

'''
숨바꼭질과 유사한 문제.
A를 시작 노드, B를 도착 노드, 가능한 연산 결과를 인접 노드로 생각하고 bfs 탐색을 적용하면 된다.

다만! 주어진 범위가 1 <= A < B <= 10**9 라서 해오던 대로 방문 리스트를 만들면 메모리 초과가 난다.
그래서 대신 방문 여부를 표시할 딕셔너리를 만들고 x를 방문하면 x를 key로, 연산 횟수를 value로 하는 요소를 추가해주었다.
'''


# A -> B가 가능하다면 필요한 연산의 최소값에 1을 더한 값을 반환하고 불가능한 경우 -1을 반환하는 함수
def bfs():
    visited = dict()                    # 방문 딕셔너리
    visited[A] = 1                      # 출발점 방문 처리
    Q = deque([A])                      # 출발점 enqueue

    while Q:                            # Q가 빌 때까지
        now = Q.popleft()                   # 현재 숫자
        for nxt in [now*2, now*10+1]:           # 가능한 연산 결과 중
            if 0 < nxt < B and not visited.get(nxt):   # 미방문한 곳이 있으면
                visited[nxt] = visited[now] + 1         # 지금까지의 연산 횟수 기록
                Q.append(nxt)                           # enqueue
            elif nxt == B:                          # B에 도착한 경우
                return visited[now] + 1                 # 연산 횟수 + 1 반환

    return -1   # B에 도착하지 못하고 탐색이 종료되면 -1 반환


A, B = map(int, input().split())    # 입력
print(bfs())                        # 계산 및 출력