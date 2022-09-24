import sys
input = sys.stdin.readline

L = int(input())                              # 원소의 개수
S = list(map(int, input().split())) + [0]     # 원소 리스트
S.sort()                                      # 오름차순 정렬
n = int(input())            

for i in range(L+1):                    # 원소를 순회하면서
    if S[i] >= n:                           # n 이상인 원소를 만나면
        if S[i] == n:                           # n이 S의 원소인 경우
            ans = 0                                 # 좋은 구간이 존재하지 않음
            break
        '''
        n보다 더 작은 원소를 포함하는 경우의 수는 0부터 l-1까지 l개, 
        더 큰 원소를 포함하는 경우의 수는 0부터 r-1까지 r개.
        좋은 구간은 l * r에서 l과 r이 둘 다 0이 되는 한 가지 경우를 뺀 개수만큼 존재한다.
        '''
        l, r = n - S[i-1], S[i] - n             
        ans = max(0, l * r - 1)
        break
print(ans)