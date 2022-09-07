import sys
input = sys.stdin.readline

'''
1. 한 글자씩 차례대로 stack에 push
2. push한 글자가 폭발 문자열의 마지막 글자와 같다면 stack의 맨 뒷 글자부터 폭발 문자열의 길이만큼 검사
3. 폭발 문자열과 일치하면 폭발 문자열의 길이만큼 pop, 아니면 pass
'''

string = input().rstrip()               # 전체 문자열
explode = list(input().rstrip())        # 폭발 문자열
N = len(explode)                        # 폭발 문자열의 길이
stk = []
for char in string:                     # 전체 문자열의 글자를 순회하면서
    stk.append(char)                        # push
    if char == explode[-1] and stk[-N:] == explode:      # stk[-N:] 이 폭발 문자열과 일치하면
        del stk[-N:]                                          # pop
if stk:
    print(*stk, sep='')
else:
    print("FRULA")