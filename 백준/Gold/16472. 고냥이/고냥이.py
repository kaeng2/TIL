from collections import defaultdict

'''
투 포인터!
'''

N = int(input())            # 인식할 수 있는 알파벳의 종류의 최대 개수
string = input()            # 문자열
s, e = 0, 0                 # 부분 문자열의 시작 인덱스, 끝 인덱스
t = 1                       # 부분 문자열 내의 알파벳 종류의 개수
alpha = defaultdict(int)    # 부분 문자열 내의 {알파벳: 개수}
alpha[string[0]] += 1
ans = 1                     # 알파벳의 종류가 N 이하인 부분 문자열의 최대 길이

while s <= e < len(string):

    if t <= N:                          # 알파벳 종류가 N개 이하이면
        ans = max(ans, e-s+1)               # ans 갱신
        if e == len(string) - 1:            # e가 맨 끝까지 왔으면
            break                               # 더 볼 필요 없다.
        e += 1                              # 부분 문자열을 늘려본다.
        if alpha[string[e]] == 0:           # 새롭게 추가된 글자가 이전 글자들과 중복되지 않으면
            t += 1                              # 알파벳 종류 개수 1 추가
        alpha[string[e]] += 1               # 딕셔너리도 추가

    else:                               # 알파벳 종류가 N개를 넘으면
        if alpha[string[s]] == 1:           # 기존 시작점에 있던 글자를 빼 버리고
            t -= 1
        alpha[string[s]] -= 1
        s += 1                              # 시작점을 앞당긴다.
print(ans)