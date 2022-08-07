# 테스트 케이스 개수    
test = int(input())
# 테스트 케이스마다
for t in range(1, test+1):
    # 테스트 케이스 번호부터 출력하고
    print(f'#{t}', end=' ')
    # 퍼즐 크기, 단어 길이
    N, K = map(int, input().split())
    # rows = [[첫째 행], [둘째 행], ...]
    # 각 행은 '0 0 1 1 1' 처럼 공백이 있는 문자열 형태
    rows = [input() for _ in range(N)]  
    
    # cols = [(첫째 열), (둘째 열), ...]
    # 각 열은 '0', '0', '1', '1', '1' 처럼 여러 문자열의 리스트 형태         
    cols = list(zip(*[row.split() for row in rows]))
    
    count = 0
    for i in range(N):
        # 각 행에서 공백을 제거하고, 0을 기준으로 쪼갠다
        # 그 중 k번 연속된 1이 몇 개나 있는지 센다 
        count += rows[i].replace(" ", "").split('0').count('1'*K)
        # 각 열을 공백 없이 합치고, 0을 기준으로 쪼갠다
        # 그 중 k번 연속된 1이 몇 개나 있는지 센다 
        count += ''.join(cols[i]).split('0').count('1'*K)
    print(count)