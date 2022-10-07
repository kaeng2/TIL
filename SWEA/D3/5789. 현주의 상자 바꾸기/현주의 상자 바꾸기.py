# 테스트 케이스 개수
test = int(input())
# 각 테스트 케이스마다
for t in range(1, test+1):
    # 상자 개수 N과 작업 횟수 Q를 입력 받고,
    N, Q = map(int, input().split())
    # 0이 N개 들어 있는 리스트를 만들자
    boxes = [0] * N
    # Q번의 작업 중 한 번의 작업마다
    for i in range(1, Q+1):
        # L과 R을 입력 받고
        L, R = map(int, input().split())
        # 해당하는 상자의 값을 i로 바꿔준다
        boxes[L-1:R] = [i]*(R-L+1)
    print(f'#{t}', *boxes)