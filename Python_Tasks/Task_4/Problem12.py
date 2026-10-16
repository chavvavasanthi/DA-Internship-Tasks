# Problem Name: 
# HackerRank Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(arr):
    distinct_heights = set(arr)
    result = sum(distinct_heights) / len(distinct_heights)
    return round(result, 3)
   
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

