def is_babygin(cards):
    count = [0]*10
    for card in cards:
        count[card] += 1
    i = 0
    babygin = 0
    while i < 10 and babygin < 2:
        # triplet 삭제
        if count[i] >= 3:
            count[i] -= 3
            babygin += 1
            continue
        # run 삭제
        if i < 8:
            if count[i] and count[i+1] and count[i+2]:
                count[i] -= 1
                count[i+1] -= 1
                count[i+2] -= 1
                babygin += 1
                continue
        i += 1
    if babygin == 2:
        return 1
    else:
        return 0        
            
test = int(input())
for t in range(1, test+1):
    print(f'#{t}', end=' ')
    cards = list(map(int, input()))
    count = [0]*10
    print(is_babygin(cards))
    
    
################################

def is_babygin(cards):
    cards.sort()
    cards1 = cards[:3]
    cards2 = cards[3:]
    if sum(cards1)/3 == cards1[1] and sum(cards2)/3 == cards2[1]:
        return 1
    elif sum(cards)/6 == cards[2] and cards[-1] - cards[0] == 2:
        return 1
    else:
        return 0

test = int(input())
for t in range(1, test+1):
    print(f'#{t}', end=' ')
    cards = list(map(int, input()))
    print(is_babygin(cards))