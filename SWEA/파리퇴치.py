 ############ sum, max 함수 없이 풀기 ############

# iterable의 원소의 합을 구하는 함수
def my_sum(iterable):
    total = 0
    for elem in iterable:
        total += elem
    return total

# 테스트 케이스 개수
test = int(input())
# 테스트 케이스마다
for t in range(1, test+1):
    # 배열의 크기, 파리채 크기
    N, M = map(int, input().split())
    # rows = [[첫째 행], [둘째 행], ...]
    rows = [list(map(int, input().split())) for _ in range(N)]
    # 각 행 내에서 연속한 M칸의 합을 기록한 리스트
    # lst1 = [ [첫 행의 첫 M칸의 합, 두 번째 M칸의 합, ...], [둘째 행의 첫 M칸의 합, 두 번째 M칸의 합, ...], ... ]
    lst1 = [[my_sum(row[i:i+M]) for i in range(N-M+1)] for row in rows]
    # lst2 = [ [첫 행의 첫 M칸의 합, 둘째 행의 첫 M칸의 합], [첫째 행의 두 번째 M칸의 합, 둘째 행의 두번째 M칸의 합], ... ]
    lst2 = list(zip(*lst1))
    mx = 0
    # M*M 사각형의 합 = lst2의 원소 M개의 합
    # lst2 내에서 가능한 M개의 합 중 최대값 구하기
    for col in lst2:
        for i in range(N-M+1):
            if mx < my_sum(col[i:i + M]):
                mx = my_sum(col[i:i + M])
    print(f'{t} {mx}')

