import sys
input = sys.stdin.readline
from collections import deque


# 가능한 모든 비밀번호를 출력하는 함수
def bck_trk():
    if len(password) == L:                                  # 비밀번호가 완성되면
        vl_cnt = len([x for x in password if x in vowels])      # 모음의 개수를 세고
        if vl_cnt >= 1 and L - vl_cnt >= 2:                     # 모음과 자음 개수 조건을 만족하면
            print(*password, sep='')                            # 출력
        return
    for i in range(C):
        if not password or max(password) < letter[i]:   # 중복되지 않고 이전 글자들보다 사전 순서가 뒤인 글자라면
            password.append(letter[i])                      # password에 추가
            bck_trk()                                       # 이 상태에서 다시 가능한 글자 탐색
            password.pop()                                  # 종료 조건이 만족되면 dequeue


L, C = map(int, input().split())        # 비밀번호 길이, 글자 개수
letter = input().split()                # 글자 종류
letter.sort()                           # 사전순 정렬
vowels = ['a', 'e', 'i', 'o', 'u']      # 모음 리스트
password = deque()                      # password를 담을 리스트 생성
bck_trk()                               # 가능한 모든 비밀번호 출력