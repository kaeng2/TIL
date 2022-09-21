import sys
input = sys.stdin.readline


N, S = map(int, input().split())            # 수열의 길이, 부분 합 최소 기준
nums = list(map(int, input().split()))
if sum(nums) < S:                           # 아예 불가능한 경우
    ans = 0
else:
    ans = N                                     # 부분 합이 S 이상인 수열의 최소 길이
    s, e = 0, 0                                 # 부분 수열의 첫 부분 인덱스, 끝 부분 인덱스
    partial_sum = nums[0]                       # partial_sum = sum(nums[s:e+1])
    while s <= e < N:
        if partial_sum < S and e < N-1:         # 부분 합이 모자라고 e의 위치가 맨 끝이 아니라면
            e += 1                                  # 끝 포인터를 한 칸 늘린다.
            partial_sum += nums[e]                  # 부분 합도 nums[e]만큼 늘어난다.
        elif partial_sum >= S:                  # 부분 합이 S 이상이면
            ans = min(ans, e-s+1)                   # 부분 합이 S를 달성했으므로 이 때의 수열 길이가 최소라면 기록한다.
            if ans == 1:                            # ans가 이미 1이라면 종료
                break
            partial_sum -= nums[s]                  # 앞 포인터를 한 칸 땡긴다. 부분 합은 맨 앞 칸만큼 빠진다.
            s += 1
        else:                                   # 부분 합이 모자란데 e가 맨 끝에 와 있다면
            break                                   # 종료
print(ans)