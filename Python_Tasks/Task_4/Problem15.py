# Problem Name:Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem

import collections

def solve():
    n = int(input())
    word_count = collections.OrderedDict()

    for _ in range(n):
        word = input().strip()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(len(word_count))
    print(*(word_count.values()))

if __name__ == "__main__":
    solve()

