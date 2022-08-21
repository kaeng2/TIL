N = int(input())        # 입력
min_cal = [0] * (N+1)   # 최소 연산 횟수를 기록
for n in range(2, N+1):
    if n % 2 and n % 3:                 # 2의 배수도 아니고 3의 배수도 아닌 경우
        min_cal[n] = min_cal[n-1] + 1
    elif n % 2 == 0 and n % 3 == 0:     # 6의 배수인 경우
        min_cal[n] = min(min_cal[n-1], min_cal[n // 2], min_cal[n // 3]) + 1
    elif n % 2 == 0:                    # 2의 배수이면서 3의 배수는 아닌 경우
        min_cal[n] = min(min_cal[n-1], min_cal[n // 2]) + 1
    else:                               # 3의 배수이면서 2의 배수는 아닌 경우
        min_cal[n] = min(min_cal[n - 1], min_cal[n // 3]) + 1
# 출력
print(min_cal[N])