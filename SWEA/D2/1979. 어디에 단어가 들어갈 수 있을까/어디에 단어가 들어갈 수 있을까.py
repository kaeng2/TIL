# 테스트 케이스 개수    
test = int(input())
# 테스트 케이스마다
for t in range(1, test+1):
    # 테스트 케이스 번호부터 출력하고
    print(f'#{t}', end=' ')
    # 퍼즐 크기, 단어 길이
    N, K = map(int, input().split())
    # rows = [[첫째 행], [둘째 행], ...]
    rows = [input() for _ in range(N)]            
    # cols = [(첫째 열), (둘째 열), ...]
    cols = list(zip(*[row.split() for row in rows]))
    count = 0
    for i in range(N):
        count += rows[i].replace(" ", "").split('0').count('1'*K)
        count += ''.join(cols[i]).split('0').count('1'*K)
    print(count)