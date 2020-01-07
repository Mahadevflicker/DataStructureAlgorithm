# Simple Linear Search algorithm being implemented with simple function
# https://www.geeksforgeeks.org/analysis-of-algorithms-set-2-asymptotic-analysis/
# Created by Mahadevan

def SimpleLinear(arr, x):

    for i in range(0,len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [23, 54, 34, 89]
x = 34

print(x, "is present in the index ", SimpleLinear(arr, x))
