# 풀이 1

# 선택정렬 함수
def selec_sort(numbers):
    N = len(numbers)
    for i in range(N - 1):
        # 기준 위치
        idx_min = i
        # 기준 위치와 나머지를 비교하면서 가장 작은 칸의 인덱스를 저장
        for j in range(i + 1, N):
            if numbers[idx_min] > numbers[j]:
                idx_min = j
        # 기준 위치와 최소 위치의 값을 교환
        numbers[i], numbers[idx_min] = numbers[idx_min], numbers[i]
    return numbers


# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test + 1):
    # 입력 받기
    N = int(input())
    nums = list(map(int, input().split()))
    # 오름차순 정렬
    nums = selec_sort(nums)
    # 테스트 케이스 번호부터 출력하고
    print(f'#{t}', end=' ')
    # 제일 큰 수와 제일 작은 수를 차례로 출력하고 리스트에서 제거
    # 10개까지 반복
    while len(nums) > N - 10:
        print(nums.pop(-1), end=' ')
        print(nums.pop(0), end=' ')
    print()

##################################################################################
# 풀이 2

# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # 입력 받기
    N = int(input())
    nums = list(map(int, input().split()))
    print(f'#{t}', end=' ')
    cnt = 0
    # 10개까지만 출력
    while cnt < 10:
        # 기준 위치
        idx_min, idx_max = 0, 0
        # 기준 위치와 나머지를 비교하면서 최소값과 최대값의 인덱스를 저장
        for j in range(1, len(nums)):
            if nums[idx_min] > nums[j]:
                idx_min = j
            elif nums[idx_max] < nums[j]:
                idx_max = j
        num_min, num_max = nums[idx_min], nums[idx_max]
        # 최대값 출력 후 삭제, cnt 1 올림
        print(num_max, end=' ')
        nums.remove(num_max)
        cnt += 1
        # 최소값 출력 후 삭제, cnt 1 올림
        print(num_min, end=' ')
        nums.remove(num_min)
        cnt += 1
        # 최대값과 최소값이 삭제되고 남은 숫자 중에서 또 최대 최소 출력... 반복..
    print()
