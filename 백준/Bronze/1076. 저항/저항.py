colorList = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
colors = []
for i in range(3):
    colors += [colorList.index(input())]
res = (colors[0] * 10 + colors[1]) * (10 ** colors[2])
print(res)