from collections import Counter

nums = [int(input()) % 42 for _ in range(10)]
print(len(Counter(nums)))