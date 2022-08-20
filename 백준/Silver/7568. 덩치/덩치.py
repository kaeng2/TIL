# 사람 수
N = int(input())
# 각 사람의 [인덱스, 몸무게, 키]
D = [[i] + list(map(int, input().split())) for i in range(N)]
# 몸무게가 높은 순으로 정렬 후, 키가 큰 순서로 정렬
D.sort(key=lambda x: (-x[1], -x[2]))
# rank[i] = i번 인덱스를 가진 사람의 덩치 등수
rank = [1] * N
# 각 사람마다
for i in range(N):
    # 자기보다 앞에 위치한 사람들 중에
    for j in D[:i]:
        # 자기보다 큰 덩치를 만나면 rank 값을 1 올려준다
        if D[i][1] < j[1] and D[i][2] < j[2]:
            rank[D[i][0]] += 1
# 출력
print(*rank)