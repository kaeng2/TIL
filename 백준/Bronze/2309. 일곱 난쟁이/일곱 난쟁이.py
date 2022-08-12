dwarfs = [int(input()) for _ in range(9)]
clue = sum(dwarfs) - 100
i, j = 0, 1

for i in range(9):
    for j in range(i+1, 9):
        if dwarfs[i] + dwarfs[j] == clue:
            fake1, fake2 = dwarfs[i], dwarfs[j]
            dwarfs.remove(fake1)
            dwarfs.remove(fake2)
            break
    else:
        continue
    break
dwarfs.sort()
print(*dwarfs, end='\n')