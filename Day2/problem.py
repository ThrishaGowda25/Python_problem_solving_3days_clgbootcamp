from collections import Counter

nums = list(map(int, input().split()))
freq = Counter(nums)

print(freq)
