from collections import deque

'''
R은 배열의 순서를 뒤집는 함수이므로, 짝수번 실행하면 아무 효과가 없다는 점에 착안하여 풀이했다.
'''

T = int(input())
for t in range(T):
    func = input().replace('RR', '')        # 배열을 연속 두 번 뒤집으면 아무 변화가 없다
    n = int(input())                        # 배열 내 수의 개수
    
    if n < func.count('D'):                 # 배열에 들어있는 수의 개수보다 많이 버리면 에러
        print('error')
        arr = input()
        continue                                # 다음 테스트 케이스로 넘어간다
    
    arr = deque(input().lstrip('[').rstrip(']').split(','))  # 숫자만 입력 받는다
    r = 0                                                    # 지금까지 나온 R의 개수
    
    # 숫자 버리기
    for p in func:
        if p == 'R':                    # R 함수인 경우
            r += 1                          # 지금까지 나온 R의 개수 + 1
        else:                           # D 함수인 경우
            if r % 2:                       # R이 홀수번 나왔다면 가장 마지막 수를 버린다
                arr.pop()
            else:                           # R이 짝수번 나왔다면 가장 처음 수를 버린다
                arr.popleft()
    # 정렬
    if r % 2:                           # R이 홀수번 나왔다면
        arr = ','.join(reversed(arr))       # 배열의 순서를 뒤집는다
    else:                               # R이 짝수번 나왔다면
        arr = ','.join(arr)                 # 순서를 유지한다
    # 출력
    print(f'[{arr}]')