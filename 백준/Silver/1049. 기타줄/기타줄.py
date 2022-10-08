import sys
input = sys.stdin.readline


N, M = map(int, input().split())                                # 끊어진 기타줄의 개수, 기타줄 브랜드의 개수
p, s = N // 6, N % 6                                            # 패키지 개수, 남은 낱개 개수
cost_p, cost_s = 6000 * p, 1000 * s
for _ in range(M):
    price = tuple(map(int, input().split()))                    # (패키지 가격, 낱개 가격)
    cost_p = min(cost_p, price[0] * p, price[1] * 6 * p)        # p개의 패키지를 사는 데에 필요한 최소 비용
    cost_s = min(cost_s, price[0], price[1] * s)                # s개의 낱개를 사는 데에 필요한 최소 비용
print(cost_p + cost_s)