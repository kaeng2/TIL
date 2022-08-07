# 10번 실행
for i in range(10):
    # 테스트 케이스 번호
    test = int(input())
    # rows = [[첫째 행], [둘째 행], [셋째 행], ...]
    rows = [list(input()) for _ in range(100)]
    # cols = [(첫째 열), (둘째 열), (셋째 열), ...]
    cols = list(zip(*rows))
    
    # 길이가 100인 회문부터 길이가 2인 회문까지 차례대로 검사
    # 첫째 행과 열부터 검사해서 회문이 나오면 반복문을 멈추고 그대로 회문 길이를 반환
    # 회문이 안 나오면 길이를 1 줄여서 다시 검사
    length = 100
    while length > 1:
        n = 0 # 현재 검사 중인 행, 열의 index
        while n < 100:
            # 각 행, 열의 가능한 단어 중 첫번째부터 검사
            for idx in range(101-length):
                words = [rows[n][idx:idx+length], cols[n][idx:idx+length]]
                if words[0] == words[0][::-1] or words[1] == words[1][::-1]:
                    longest = length # 회문 나오면 그 때의 회문 길이를 longest에 저장
                    # 모든 반복문을 종료
                    length = 1
                    n = 100
                    break
            # 회문이 한 번도 안나오면 index를 하나 늘려서 다음 행, 열 검사
            else:
                n += 1
        # 모든 행과 열을 검사하는 동안 length 길이의 회문이 없었다면 length를 하나 줄여서 다시 검사 반복
        length -= 1
    print(f'#{test} {longest}')