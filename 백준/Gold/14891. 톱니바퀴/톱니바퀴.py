import sys
input = sys.stdin.readline

# 입력
wheels = [input().replace('\n', '') for _ in range(4)]  # wheels[i] = i번째 톱니바퀴의 정보
K = int(input())    # 회전 횟수
rotations = [list(map(int, input().split())) for _ in range(K)] # rotations[i] = [회전시킬 톱니바퀴의 번호, 회전 방향]

indicators = {x: [6, 2] for x in range(4)}  # indicators[i] = [i번째 톱니바퀴 중 왼쪽 바퀴와 맞물린 톱니의 index, 오른쪽 바퀴와 맞물린 톱니의 index]


# 서로 맞닿은 두 톱니의 극이 다른지 여부를 반환하는 함수
def get_is_chaining():
    # is_chaining[i] = i번째 톱니바퀴와 i+1번째 톱니바퀴가 서로 다른 극으로 맞닿아 있으면 True, 아니면 False
    is_chaining = []
    
    for i in range(3):
        is_chaining += [bool(wheels[i][indicators[i][1]] != wheels[i+1][indicators[i+1][0]])]
    return is_chaining

# 특정 톱니바퀴를 회전시키는 함수
def rotate(wheel_num, direction):
    indicators[wheel_num] = [(x - direction + 8 * int(direction == 1)) % 8 for x in indicators[wheel_num]]
    return
    

# 주어진 회전에 대해 실행
for target, dir in rotations:
    is_chaining = get_is_chaining()
    target -= 1
    # 타겟 톱니바퀴 회전
    rotate(target, dir)
    # 왼쪽 톱니바퀴 회전
    reverse_dir = dir
    for i in range(target-1, -1, -1):
        if is_chaining[i]:
            reverse_dir *= (-1)
            rotate(i, reverse_dir)
        # 왼쪽 톱니바퀴와 맞물린 극이 같다면 더 이상 회전이 퍼지지 않음
        else:
            break
    # 오른쪽 톱니바퀴 회전
    reverse_dir = dir
    for j in range(target, 3):
        if is_chaining[j]:
            reverse_dir *= (-1)
            rotate(j+1, reverse_dir)
        # 오른쪽 톱니바퀴와 맞물린 극이 같다면 더 이상 회전이 퍼지지 않음
        else:
            break
score = 0        
for n in range(4):
    north = (indicators[n][0] + 2) % 8
    score += int(wheels[n][north]) * (2**n)

print(score)