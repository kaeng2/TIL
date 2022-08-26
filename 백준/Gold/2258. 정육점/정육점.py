N, M = map(int, input().split())                            # 고깃덩이 개수, 필요한 고기 양
meat = [list(map(int, input().split())) for _ in range(N)]  # meat[i] = [무게, 가격]
meat.sort(key=lambda x: (x[1], -x[0]))                      # 가격 오름차순 후, 무게 내림차순 정렬
weight, price = [x[0] for x in meat], [x[1] for x in meat]
if sum(weight) < M:     # 불가능한 경우
    print(-1)
else:
    cart, cost, same, ans = weight[0], price[0], 0, sum(price)  # 초기값 설정
    for i in range(1, N):
        cart += weight[i]                          
        if price[i] > price[i-1]:    # 이전 고기보다 가격이 비싼 경우
            cost = price[i]             # 이전 고기들은 덤이 되고, 현재 고기의 가격만큼만 지불하면 된다
        else:                        # 이전과 가격이 같은 경우
            cost += price[i]            # 가격이 같은 고기는 추가로 비용을 지불해야 한다
        if cart >= M:                # 필요한 무게를 채웠을 경우
            ans = min(ans, cost)        # 최소값 갱신
    print(ans)