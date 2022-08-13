cnt = 0
for i in range(8):
    if i%2:
        line = input()[1::2]
    else:
        line = input()[::2]
    cnt += line.count('F')

print(cnt)