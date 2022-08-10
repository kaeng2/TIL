n = int(input())
rows = [[0]*100 for _ in range(100)]
for i in range(n):
    x, y = map(int, input().split())
    for j in range(y, y+10):
        rows[y][x:x+10] = [1]*10
area = 0
for row in rows:
    area += row.count(1)
print(area)
