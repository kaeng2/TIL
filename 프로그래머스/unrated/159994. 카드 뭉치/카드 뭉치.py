from collections import deque

def choose_card_set(set1, set2, target):
    if set1 and set1[0] == target:
        return set1
    if set2 and set2[0] == target:
        return set2
    return False
    
def use_card_from(card_set, targets):
    card_set.popleft()
    targets.popleft()
    
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    while goal:
        card_set = choose_card_set(cards1, cards2, goal[0])
        if card_set:
            use_card_from(card_set, goal)
        else:
            return "No"
    
    return "Yes"