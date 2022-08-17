# 입력
A, B = map(int, input().split())
# 소인수 개수
cnt = [0] * (B+1)
# B 이하의 소수 리스트
lst = [0, 0] + list(range(2, B))
d = 2
while d**2 <= B:
    lst[d**2::d] = [0] * len(lst[d**2::d])
    d += 1
prime_nums = [x for x in lst if x]
# 소수의 소인수 개수는 1
for p in prime_nums:
    cnt[p] = 1
# 소수에 다른 소수가 하나 곱해질 때마다 소인수 개수를 1 추가함
for p in prime_nums:
    i = 2
    while i * p <= B:
        if cnt[i] and cnt[i * p] == 0:
            cnt[i * p] = cnt[i] + 1
        i += 1
# 소인수의 개수가 소수 리스트 내에 있으면 언더프라임 개수를 1 높인다
# 최소 소수인 2만 17번 결합해도 가능한 최대값인 100,000을 넘어가므로
# 언더프라임의 경우 가능한 최대 소인수 개수는 13개이다
under_p = 0
for n in range(A, B+1):
    if cnt[n] in [2, 3, 5, 7, 11, 13]:
        under_p += 1
# 출력
print(under_p)