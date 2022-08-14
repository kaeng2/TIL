# 가장 높은 기둥 기준으로 왼쪽의 면적을 구하는 함수
def left_area(loca, height, first_max_idx):
    if first_max_idx == 0:
        return 0
    # nxt_i = 가장 높은 기둥의 왼쪽에서 가장 높은 기둥의 인덱스
    # 가장 높은 기둥이 여러 개일 경우 가장 왼쪽의 인덱스를 저장
    nxt_i = height.index(max(height[:first_max_idx]))
    # nxt_i 기준으로 면적을 계산한 후
    # nxt_i 왼쪽에서 다시 가장 높은 기둥을 찾고 면적을 계산하는 작업을 반복
    area = abs(loca[first_max_idx] - loca[nxt_i]) * height[nxt_i] + left_area(loca, height, nxt_i)
    return area


# 입력
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
# 위치 순서대로 정렬
lst.sort(key=lambda x: x[0])
# 위치만 모은 리스트
loca = [x for x, y in lst]
# 높이만 모은 리스트
height = [y for x, y in lst]
# 최대 높이를 가진 기둥들의 인덱스를 전부 추출
max_idx = list(filter(lambda i: height[i] == max(height), range(len(height))))
# 최대 높이 기둥 중 가장 왼쪽에 있는 기둥을 기준으로 왼쪽의 면적
lft = left_area(loca, height, max_idx[0])
# 최대 높이 기둥 중 가장 오른쪽에 있는 기둥을 기준으로 오른쪽의 면적
rgt = left_area(list(reversed(loca)), list(reversed(height)), len(lst)-1 - max_idx[-1])
# 최대 높이 기둥끼리의 면적
mid = (loca[max_idx[-1]] - loca[max_idx[0]] + 1) * max(height)
print(lft + rgt + mid)