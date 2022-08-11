for _ in range(10):
    t = int(input())
    rows = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    goal = rows[-1].index(2)
    for i in range(98, 0, -1):
        if rows[i][goal-1] == 1:
            while rows[i][goal-1] == 1:
                goal -= 1
        elif rows[i][goal+1] == 1:
            while rows[i][goal+1] == 1:
                goal += 1
    print(f'#{t} {goal-1}')
