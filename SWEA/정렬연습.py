# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # N과 N개의 숫자열을 입력받는다
    N = int(input())
    nums = list(map(int, input().split()))
    # 테스트 케이스 번호부터 출력
    # 끝에 줄바꿈이 아닌 공백을 준다.
    print(f'#{t}', end=' ')
    # 전체 리스트에서 범위를 줄여가면서
    for n in range(N, 1, -1):
        # 한 원소가 다음 원소보다 크면 두 원소의 자리를 교환한다
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    # 출력 양식에 맞게 출력한다.
    for num in nums:
        print(num, end=' ')
    print()
    
    
    