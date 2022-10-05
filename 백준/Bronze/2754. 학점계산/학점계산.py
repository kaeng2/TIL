grade = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, '+': 0.3, '0': 0.0, '-': -0.3}
g = list(input())
if len(g) == 1:
    print(0.0)
else:
    print(grade[g[0]]+grade[g[1]])