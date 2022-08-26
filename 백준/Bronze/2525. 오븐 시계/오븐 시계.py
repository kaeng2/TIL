h_table = list(range(24))
h, m = map(int, input().split())
cooking = int(input())
if cooking % 60 + m >= 60:
    m = m + cooking % 60 - 60
    h += 1
else:
    m += cooking % 60
h = h_table[(h + cooking // 60) % 24]
print(h, m)