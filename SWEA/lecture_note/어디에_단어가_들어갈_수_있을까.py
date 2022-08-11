######### count 메서드 안 쓰고 풀기 #########

# iterable 내의 특정 원소의 개수를 찾는 함수 정의
def my_count(x, iterable):
    my_cnt = 0
    for elem in iterable:
        if elem == x:
            my_cnt += 1
    return my_cnt

# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # 배열 크기, 단어 길이
    N, K = map(int, input().split())
    # 문자열의 공백을 제거한 형태의 행 모음
    rows = [input().replace(' ', '') for _ in range(N)]
    # 문자열의 공백을 제거한 형태의 열 모음
    cols = [''.join(x) for x in list(zip(*rows))]
    cnt = 0
    # 각 행과 열을 0을 기준으로 split
    # 그 중 1이 K개만큼 연속한 원소가 몇 개 있는지 확인
    for i in range(N):
        cnt += my_count('1'*K, rows[i].split('0')) + my_count('1'*K, cols[i].split('0'))
    print(f'#{t} {cnt}')
