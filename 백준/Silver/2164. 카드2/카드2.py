from collections import deque

N = int(input())
cards = deque(range(1, N+1))
while len(cards) > 1:            # 카드가 한 장 남을 때까지 반복
    cards.popleft()                  # 맨 위의 한 장 버린다
    cards.append(cards.popleft())    # 그 다음 카드는 맨 뒤로 보낸다
print(*cards)