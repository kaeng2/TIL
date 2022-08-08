def harvest(farm, N):
    # 가운데 지점의 인덱스
    med = (N-1) // 2
    # h는 가운데를 기준으로 양 옆 몇 칸씩 수확할건지를 나타내는 숫자의 모음
    # 0부터 med까지 1씩 커졌다가 다시 1씩 작아지는 형태
    # h = [0, 1, 2, 3, 2, 1, 0] 과 같은 형태
    h = list(range(med)) + list(range(med, -1, -1))
    harvested = 0
    for i in range(N):
        harvested += sum(farm[i][med-h[i]: med+1+h[i]])
    return harvested
    
test = int(input())
for t in range(1, test+1):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]
    crop = harvest(farm, N)
    print(f'#{t} {crop}')
