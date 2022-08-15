# 입력
N = int(input())
# 5kg 봉지를 최대로 가져가보고 남은 설탕량을 3kg 봉지로 가져갈 수 있는지 확인
for i in range(N // 5, -1, -1):
    # 불가능 하다면 5kg 봉지를 하나씩 줄여가면서 확인
    if (N - (5*i)) % 3:
        continue
    # 가능한 경우 결과 출력 후 반복문 종료
    else:
        result = i + (N-(5*i))//3
        print(result)
        break
# 모든 경우 불가능 하다면 -1 출력
else:
    print(-1)