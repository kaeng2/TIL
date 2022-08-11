# 각 테스트 케이스마다
for i in range(10):
    # 덤프 횟수 int로 입력 받자
    num_dump = int(input())
    # 상자 높이값을 list로 입력 받자
    ls = list(map(int, input().split()))

    # 덤프 한 번 할 때마다
    for dump in range(num_dump):
        # 상자 높이값을 큰 순서대로 정렬하고
        ls.sort(reverse=True)
        if ls[0] - ls[-1] <= 1:
            print(f'#{i + 1} 0')
            break
        # 제일 큰 애는 1만큼 줄이고
        ls[0] -= 1
        # 제일 작은 애는 1만큼 더해준다.
        ls[-1] += 1
        # 다시 큰 순서대로 정렬 해준다.
        ls.sort(reverse=True)

    # 모든 dump가 끝나고 나면 상자 높이값 중 최대값과 최소값의 차이를 출력한다.
    print(f'#{i + 1} {ls[0] - ls[-1]}')