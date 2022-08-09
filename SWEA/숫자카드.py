# 테스트 케이스 개수
test = int(input())
for t in range(1, test+1):
    # 입력 받기
    N = int(input())
    nums = input()
    # 카드 별 장수 세기
    cnt = [0]*10
    for i in nums:
        cnt[int(i)] = nums.count(i)
    # 가장 많이 나온 카드의 장수
    howmany = max(cnt)
    # 가장 많이 나온 카드의 숫자
    cnt.reverse()
    mx = 9 - cnt.index(howmany)
    
    print(f'#{t} {mx} {howmany}')