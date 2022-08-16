# 각 테스트 케이스마다
for t in range(1, 11):
    # 테스트 케이스 길이
    N = int(input())
    # 괄호 문자열 입력
    string = input().replace('()', '').replace('{}', '').replace('<>', '').replace('[]', '')
    p_dict = {'(': ')', '{': '}', '<': '>', '[': ']'}
    i = 0
    # 괄호 짝이 있으면 둘 다 제거
    while string:
        k = string[i]
        # 닫는 괄호일 경우
        if p_dict.get(k, 0) == 0:
            print(f'#{t} 0')
            break
        # 여는 괄호지만 짝이 없는 경우
        elif string[i+1:].count(p_dict[k]) == 0:
            print(f'#{t} 0')
            break
        # 이 외의 경우에는 짝을 지우자
        else:
            string = string.replace(k, '', 1).replace(p_dict[k], '', 1)
    else:
        print(f'#{t} 1')