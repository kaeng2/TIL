import sys
input = sys.stdin.readline
import heapq

'''
우선순위 큐를 이용한 위상정렬 풀이
'''

N, M = map(int, input().split())        # 문제 개수, 정보 개수
after = [[] for _ in range(N+1)]        # after[i] = i번 문제를 풀고나서 풀어야 할 문제 목록
before = [0] * (N+1)                    # before[i] = i번 문제를 풀기 전에 풀어야 할 문제 수
Q = set(range(1, N+1))                  # Q에는 선행 문제가 없는 문제만 담는다.

for _ in range(M):
    A, B = map(int, input().split())
    after[A] += [B]                     # A를 풀고나서 B를 풀어야 한다. 
    before[B] += 1                      # B를 풀기 전에 풀어야 할 문제 1개 추가
    Q.discard(B)                        # B는 선행 문제가 있으므로 Q에서 삭제

Q = list(Q)
while Q:
    now = heapq.heappop(Q)              # 가능하면 쉬운 문제부터 푼다.
    print(now, end=' ')                 # 지금 푼 문제 출력
    for nxt in after[now]:              # 그 다음 풀 수 있는 문제들에 대해서
        before[nxt] -= 1                    # 선행 문제를 하나 풀었으니까 1 빼준다.
        if not before[nxt]:                 # 선행 문제를 다 푼 문제는
            heapq.heappush(Q, nxt)              # enqueue