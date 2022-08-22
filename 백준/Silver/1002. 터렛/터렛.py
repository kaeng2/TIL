# 테스트 케이스 개수
T = int(input())
# 각 테스트 케이스마다
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())  # 좌표 및 류재명과의 거리
    # 변수 생성
    d_square = (x1 - x2)**2 + (y1 - y2)**2     # 두 좌표(조규현과 백승환) 사이의 거리의 제곱
    in_circle = (abs(r1 - r2))**2              # 내접을 판단할 기준값 (제곱)
    circum_circle = (r1 + r2)**2               # 외접을 판단할 기준값 (제곱)
    # 가능한 류재명 위치의 수
    if r1 == r2 and (x1, y1) == (x2, y2):                     # 두 원이 완전히 일치하는 경우
        result = -1
    elif d_square < in_circle or circum_circle < d_square:    # 두 원의 접점이 없는 경우
        result = 0
    elif in_circle < d_square < circum_circle:                # 두 원의 교점이 2개인 경우
        result = 2
    elif d_square == in_circle or d_square == circum_circle:  # 두 원이 내접 혹은 외접하는 경우
        result = 1
    # 출력
    print(result)