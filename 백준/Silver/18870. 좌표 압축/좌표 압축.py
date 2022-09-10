import sys
input = sys.stdin.readline
from collections import Counter

'''
Counter(iterable)은 iterable 내의 원소와 동일한 원소 개수가 각각 key, value인 딕셔너리이다.
이 문제에서는 더 작은 좌표의 개수를 셀 때 중복되는 좌표는 무시하기 때문에 { 원소 : 1 } 의 형태로 구성된 딕셔너리를 사용해도 무방하다.
하지만 굳이 원소를 순회하면서 value값을 0으로 넣어주기 보다는 그냥 간편하게 Counter 함수를 이용했다.
중복되는 좌표도 모두 고려하는 경우라면 Counter(iterable)의 value 값이 유용하게 쓰일 것이다. 
'''


N = int(input())                        # 좌표의 개수
C = list(map(int, input().split()))     # 좌표 리스트
dict_C = Counter(C)                     # { 좌표: 해당 좌표의 개수 }
smaller = 0                             # 더 작은 좌표의 개수를 저장할 변수
for k in sorted(dict_C.keys()):         # 좌표를 오름차순으로 순회하면서
    dict_C[k] = smaller                     # dict_C[k]의 값을 smaller로 갱신
    smaller += 1                            # 다음 좌표보다 더 작은 좌표가 한 개 늘어남
# 출력
for c in C:                     # 각 좌표마다
    print(dict_C[c], end=' ')       # 자기보다 작은 좌표의 개수를 출력
