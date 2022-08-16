# 괄호 문자열이 유효한지 확인하는 함수
def is_valid(string):
    p_lst = [['(', ')'], ['{', '}'], ['<', '>'], ['[', ']']]
    cnt_lst = [0] * 4
    for i in range(4):
        for j in string:
            # 해당 글자가 여는 괄호라면 +1
            if j == p_lst[i][0]:
                cnt_lst[i] += 1
            # 닫는 괄호라면 -1
            elif j == p_lst[i][1]:
                cnt_lst[i] -= 1
            # cnt가 음수가 되는 순간 0 반환
            if cnt_lst[i] < 0:
                return 0
        # string의 모든 글자를 검사했을 때 cnt가 0이 아니라면 0 반환
        if cnt_lst[i] != 0:
            return 0
    # 모두 통과한다면 1 반환
    return 1

# 각 테스트 케이스마다
for t in range(1, 11):
    # 테스트 케이스 길이
    N = int(input())
    # 괄호 문자열 입력
    string = input().replace('()', '').replace('{}', '').replace('<>', '').replace('[]', '')
    # 결과 출력
    result = is_valid(string)
    print(f'#{t} {result}')