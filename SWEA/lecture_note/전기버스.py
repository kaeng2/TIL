T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    # 충전소 위치
    charge = list(map(int,input().split()))
    # 현재 위치
    now = 0
    # 충전 횟수
    cnt = 0
    # 도착점에 도착할 때까지
    while now < N:
        # 최대로 움직여보고 안되면 한칸씩 줄여서 움직여보자
        for move in range(K, 0, -1):
            # 도착점을 넘어가면 노선번호와 충전횟수 출력 후 반복문 종료
            if now+move >= N:
                now = N
                print(f'#{t} {cnt}')
                break 
            # 이동할 칸에 충전소가 있으면 이동하고 충전횟수를 1 추가한다.              
            elif now+move in charge:
                now += move
                cnt += 1
                break
            # 충전소가 없으면 한 칸 줄여서 움직여본다
            else:
                continue
        # 이동할 수 있는 범위를 다 찾아도 충전소가 없다면
        # 노선번호와 0을 출력하고 반복문 종료
        else:
            print(f'#{t} 0')
            break