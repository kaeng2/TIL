# 10번 실행
for _ in range(1, 11):
    # 입력
    t = input()                             # 테케 번호
    nums = list(map(int, input().split()))  # 숫자
    while nums[-1] != 0:                    # 맨 마지막 숫자가 0이 되면 그만한다
        for i in range(1, 6):                   # 한 사이클 동안 단위 작업 실행
            nums += [nums.pop(0) - i]               # 맨 앞의 수를 꺼내서 i만큼 뺀 뒤 다시 맨 뒤 순서로 넣어준다
            if nums[-1] <= 0:                       # 방금 넣어준 숫자가 0 이하라면
                nums[-1] = 0                            # 0으로 바꿔주고 종료한다
                break
    # 출력
    print(f'#{t}', *nums)