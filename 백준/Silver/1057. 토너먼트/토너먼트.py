import sys
input = sys.stdin.readline

# x번과 y번이 만날 때까지 라운드를 진행하는 함수
def match(x, y):
    global round
    
    # 현재 x번이 이길 경우 다음 라운드에서 (x+1)//2번을 배정 받음
    # 현재 y번이 이길 경우 다음 라운드에서 (y+1)//2번을 배정 받음
    nxt_x = (x+1) // 2
    nxt_y = (y+1) // 2
    
    # x번과 y번이 다음 라운드에 받을 번호가 같다면 둘은 현재 라운드에서 만난 것이므로 종료
    if nxt_x == nxt_y:
        return
    
    # 둘이 만나지 않았다면 다음 라운드 진행
    else:
        round += 1
        match(nxt_x, nxt_y)
        return
    

round = 1         # 1라운드에서 시작
N, A, B = map(int, input().split())
match(A, B)
print(round)