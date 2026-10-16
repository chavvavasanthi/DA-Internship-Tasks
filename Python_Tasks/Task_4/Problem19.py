# Problem Name: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

# Read input
X = int(input())
sizes = Counter(map(int, input().split()))
N = int(input())

earnings = 0

# Process customers
for _ in range(N):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        earnings += price
        sizes[size] -= 1

# Output result
print(earnings)




