import sys
input = sys.stdin.readline


'''
꼭짓점의 좌표로 다각형의 면적을 구하는 신발끈 공식을 이용했다.
'''
N = int(input())
vertex = [tuple(map(int, input().split())) for _ in range(N)]
vertex += [vertex[0]]
area = vertex[0][0] * vertex[1][1] - vertex[-1][0] * vertex[-2][1]
for i in range(1, N):
    area += vertex[i][0] * vertex[i+1][1] - vertex[i][0] * vertex[i-1][1]
area = abs(area) / 2
print(f'{area:0.1f}')