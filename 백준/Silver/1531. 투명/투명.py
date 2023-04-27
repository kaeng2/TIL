import sys
input = sys.stdin.readline
from itertools import chain

N, M = map(int, input().split())
sheet = [[0] * 100 for _ in range(100)]
def put_paper(r1, c1, r2, c2):
    for r in range(r1-1, r2):
        for c in range(c1-1, c2):
            sheet[r][c] += 1

def count_hidden_block():
    print(len([x for x in chain(*sheet) if x > M]))
    
papers = [list(map(int, input().split())) for _ in range(N)]
for paper in papers:
    put_paper(*paper)
count_hidden_block() 