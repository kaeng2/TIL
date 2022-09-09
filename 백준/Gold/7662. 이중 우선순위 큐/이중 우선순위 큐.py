import sys
input = sys.stdin.readline
import heapq

'''
* 준비
최소 힙과 최대 힙을 하나씩 만들고, 특정 숫자가 존재하는지 여부를 기록할 exist 배열을 만든다.

* Insert 연산
최소 힙에는 (n, id값)을, 최대 힙에는 (n, id값)을 push한다.
이 때 id값은 exist 배열에 접근할 인덱스로, 연산이 모두 끝난 후 해당 숫자가 존재하는지 확인하는 용도로 쓴다.
숫자를 insert 했으므로 exist[id] 값을 1로 갱신한다.

* Delete 연산
힙에 숫자가 있는 경우에만 연산을 진행한다.
최소값을 삭제하는 경우에는 exist[ 최소 힙[0]의 id값 ] 값을 0으로 갱신하고, 최소 힙에서 pop 해준다.
최대값을 삭제하는 경우도 마찬가지로 exist[ 최대 힙[0]의 id값 ] 값을 0으로 갱신하고, 최대 힙에서 pop 해준다.
이 때 두 힙 중에 빈 힙이 생기거나, 최소 힙[0][0]이 최대 힙[0][0]보다 크다면 모든 숫자가 삭제된 것이다.
최소 힙[0][0] = a 라는 것은 a보다 작은 수는 모두 삭제되었다는 의미이며, 마찬가지로 최대 힙[0][0] = b 라는 것은 b보다 큰 수는 모두 삭제되었다는 의미이다.
그러므로 삭제되지 않고 남아있는 정수 n은 a <= n <= b를 만족한다. 그런데 a가 b보다 커질 경우, 이러한 n이 존재하지 않으므로 모든 숫자가 삭제되었음을 의미한다.
따라서 이러한 경우 두 힙을 모두 초기화 시킨다.

# 연산 이후
이미 삭제됐지만 최소 힙이나 최대 힙에 남아있는 허수들을 pop 해준다.

# 결과 도출
힙이 비었다면 "EMPTY"를 출력하고, 그렇지 않은 경우 남아있는 숫자 중의 최대값과 최소값을 출력한다.
'''


def solve(cmd):
    min_heap, max_heap = [], []
    exist = [0] * k
    for i in range(k):
        # 연산 수행
        if cmd[i] == 'D -1':                                    # Delete minimum
            if min_heap:                                            # 최소 힙에 숫자가 있을 때만 수행
                exist[min_heap[0][1]] = 0                               # 삭제 표시
                heapq.heappop(min_heap)                                 # 최소값 삭제
            if not min_heap or min_heap[0][0] > -max_heap[0][0]:    # 숫자가 모두 삭제된 경우
                min_heap, max_heap = [], []                             # 두 힙 모두 초기화
        elif cmd[i] == 'D 1':                                   # Delete maximum
            if max_heap:                                            # 최대 힙에 숫자가 있을 때만 수행
                exist[max_heap[0][1]] = 0                               # 삭제 표시
                heapq.heappop(max_heap)                                 # 최대값 삭제
            if not max_heap or min_heap[0][0] > -max_heap[0][0]:    # 숫자가 모두 삭제된 경우
                min_heap, max_heap = [], []                             # 두 힙 모두 초기화
        else:                                                   # Insert n
            n = int(cmd[i].split()[-1])
            heapq.heappush(min_heap, (n, i))                        # 최소 힙에 push
            heapq.heappush(max_heap, (-n, i))                       # 최대 힙에 push
            exist[i] = 1                                            # insert 표시
        # 허수 제거
        while max_heap and not exist[max_heap[0][1]]:       # 최대값이 존재하는 값일 때까지 계속 pop
            heapq.heappop(max_heap)
        while min_heap and not exist[min_heap[0][1]]:       # 최소값이 존재하는 값일 때까지 계속 pop
            heapq.heappop(min_heap)
    # 출력
    if not min_heap:
        print("EMPTY")
        return
    print(-max_heap[0][0], min_heap[0][0])


T = int(input())                        # 테스트 케이스 개수
for t in range(T):
    k = int(input())                    # 연산의 개수
    cmd = []
    for _ in range(k):                  # 연산 입력
        cmd += [input().rstrip()]
    solve(cmd)