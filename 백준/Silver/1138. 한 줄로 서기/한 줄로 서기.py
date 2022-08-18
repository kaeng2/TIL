# 사람의 수
N = int(input())
# 키가 1인 사람부터 N인 사람까지 차례대로
# 자기보다 키 큰 사람이 왼쪽에 몇 명 있었는지
memory = list(map(int, input().split()))
line = [N]
# 키가 N인 사람부터 1인 사람까지 차례대로
# 자기보다 키 큰 사람이 memory[i-1]명 있도록 줄에 삽입
for i in range(N-1, 0, -1):
    line.insert(memory[i-1], i)
# 출력
print(*line)