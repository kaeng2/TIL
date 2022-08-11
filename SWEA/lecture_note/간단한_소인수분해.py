# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # 입력 받기
    N = int(input())
    # 소인수 리스트
    elem = [2, 3, 5, 7, 11]
    # [a, b, c, d, e]
    result = [0]*5
    # 각각의 소인수로 N을 가능한 한 계속 나누면서 카운트 올리기
    # 나눴을 때 나머지가 있으면 반복문 종료
    for i in range(5):
        while N % elem[i] == 0:
            N = N // elem[i]
            result[i] += 1
    # 결과 출력
    print(f'#{t}', *result)
    