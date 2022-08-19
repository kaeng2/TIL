# 테스트 케이스 개수
T = int(input())
# 각 테스트 케이스마다
for t in range(1, T+1):
    nums, change = input().split()  # 숫자판, 교환 횟수
    nums, change = list(map(int, nums)), int(change)
    N, c, r = len(nums), 0, 0       # 숫자 개수, 현재까지 누적 교환 횟수, 이미 제자리에 있어서 교환할 필요가 없는 숫자 개수
    rep = [i for i in range(N) if nums.count(nums[i]) > 1]  # 중복된 숫자의 인덱스 모아두기
    # 교환 시작
    # c가 범위를 벗어나거나 숫자판이 내림차순으로 정렬되면 종료
    while c < change and nums != sorted(nums, reverse=True):
        # 교환해서 고정 시킨 숫자를 제외한 나머지 숫자 중 최대값과 그 인덱스를 저장
        idx, mx = max(enumerate(nums[c+r:], c+r), key=lambda x: (x[1], x[0]))
        # 교환할 자리에 이미 최대값이 있는 경우 한 칸 뒤에서부터 다시 시작
        if nums[c+r] == nums[idx]:
            r += 1
            continue
        nums[c+r], nums[idx] = nums[idx], nums[c+r]     # 고정 시킨 숫자 바로 다음 숫자와 최대값을 교환
        c += 1                                          # 누적 교환 횟수 1 올리기
    # 내림차순 정렬을 못한 채로 교환 횟수를 모두 채운 경우
    if c == change:
        # rep 자리에 들어있는 숫자끼리 내림차순으로 배열
        lst = sorted([nums[i] for i in rep], reverse=True)
        for i in rep:
            nums[i] = lst.pop(0)
    # 교환이 끝났을 때 남은 교환 횟수가 홀수인데
    if (change - c) % 2:
        if len(set(nums)) == N and N > 1:               # 중복되는 숫자가 없다면
            nums[-2], nums[-1] = nums[-1], nums[-2]     # 맨 뒤 두 자리만 1회 교환
    # 결과 출력
    nums = list(map(str, nums))
    print(f'#{t} {"".join(nums)}')