import sys
input = sys.stdin.readline
import heapq


# 입력
N, K = map(int, input().split())                # 보석 개수, 가방 개수
jewel = []                                      # 보석의 (무게, 가격)을 담아둔 리스트
for i in range(N):
    M, V = map(int, input().split())
    heapq.heappush(jewel, (M, V))
bags = [int(input()) for _ in range(K)]         # bags[i] = i번째 가방의 최대 무게

# 오름차순 정렬
bags.sort()

# 훔치기
temp = []                                       # 이번 가방에 넣을 수 있는 모든 보석들을 담아두는 배열
steal = 0                                       # 훔친 보석의 가격의 총 합

for bag in bags:                                # 각 가방 채우기
    
    # 현재 가방에 넣을 수 있는 모든 보석의 가격을 temp에 enqueue
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewel)[1])
   
    # temp에 담긴 보석 중에 훔칠 보석 고르기
    if temp:
        steal -= heapq.heappop(temp)    # 가장 가격이 비싼 걸로 훔친다.
    
    # temp가 비었고 남아있는 보석도 없으면 종료
    elif not jewel:
        break
print(steal)