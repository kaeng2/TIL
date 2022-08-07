# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # Ai와 Bj의 길이
    N, M = map(int, input().split())
    # Ai와 Bj를 정수로 구성된 리스트 형태로 입력 받자
    Ai = [int(x) for x in input().split()]
    Bj = [int(y) for y in input().split()]
    # 원소끼리의 곱셈의 합을 넣어줄 리스트
    result = []
    # Ai가 더 짧으면
    if N < M:
        # 가능한 시작점에서부터
        for start in range(M-N+1):
            # Bj를 Ai의 길이와 같아지도록 자르고
            cut_Bj = Bj[start: start+N]
            # Ai와 자른 Bj의 각 원소끼리 곱하여 합해준다
            result += [sum(map(lambda x,y: x*y, Ai, cut_Bj))]
    # Bj가 더 짧을 때도 동일하게 진행한다
    elif N > M:
        for start in range(N-M+1):
            cut_Ai = Ai[start: start+M]
            result += [sum(map(lambda x,y: x*y, cut_Ai, Bj))]
    # 테스트 케이스의 번호와 결과값 중 최대값을 출력한다
    print(f'#{t} {max(result)}')
    
    
    
        
 