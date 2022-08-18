# 입력
N = int(input())
nums = list(map(int, input().split()))
# 기존 수열에 인덱스를 붙이고, 오름차순으로 정렬
# 오름차순으로 정렬된 수열에 다시 인덱스를 붙임
lst = list(enumerate(sorted(enumerate(nums), key=lambda x: x[1])))
# 기존 수열의 인덱스 대로 정렬
lst.sort(key=lambda x: x[1][0])
# 수열의 오름차순 대로 인덱스 출력
for i in lst:
    print(i[0], end=' ')