import sys
input = sys.stdin.readline
from collections import deque
import heapq

'''
먼저 서류 성적을 오름차순으로 정렬하고, 한 명씩 심사한다.
현재 지원자는 이전 지원자보다 서류 성적이 낮으므로, 면접 성적이 더 높아야만 합격한다.
합격하면 accepted 배열에 push하고, 불합격하면 버려진다.
accepted 배열에 마지막으로 push된 지원자의 면접 성적은 지금까지 심사한 지원자의 성적 중 가장 높다.
따라서 심사 시 accepted 배열에 가장 최근 push된 지원자의 면접 성적과 현재 지원자의 면접 성적만을 비교하여 합불 여부를 결정한다.
'''

T = int(input())        # 테스트 케이스 개수
for t in range(T):
    N = int(input())            # 지원자 수
    Q = []                      # 최소 힙
    for _ in range(N):
        heapq.heappush(Q, list(map(int, input().split())))      # 서류 성적 순위대로 정렬되도록 최소 힙에 enqueue
    accepted = deque([heapq.heappop(Q)])                        # 서류 1등은 무조건 합격
    for _ in range(N-1):                                        # 서류 2등부터 N등까지 심사
        applicant = heapq.heappop(Q)                                # 남은 사람들 중 서류 성적이 가장 높은 지원자 pop
        if accepted[0][1] > applicant[1]:                           # 이전 지원자의 면접 성적보다 높을 때만
            accepted.appendleft(applicant)                              # accepted에 enqueue
    print(len(accepted))                                        # 합격한 지원자 수 출력