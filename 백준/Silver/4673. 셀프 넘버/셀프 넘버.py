# 자릿수의 합을 구하는 함수
def sum_digit(n):
    if n < 10:
        return n
    digit = n % 10
    nxt = n // 10
    return digit + sum_digit(nxt)


def d(n):
    return n + sum_digit(n)

# 생성자가 있는 숫자 리스트
have_gnrt = []
# 1 ~ 9999의 숫자의 d(n)을 리스트에 저장
for i in range(1, 10000):
    have_gnrt += [d(i)]
# 1 ~ 10000의 숫자 중 generator가 있는 숫자 제외
self_num = list(set(range(1, 10001)) - set(have_gnrt))
self_num.sort()
for i in self_num:
    print(i)