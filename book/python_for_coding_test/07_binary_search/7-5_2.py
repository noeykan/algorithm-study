#251122

import sys

N = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()
M = int(sys.stdin.readline().rstrip())
query = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(arr, start, end, target):
    if start > end:
        return None
    
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, end, target)
    else:
        return binary_search(arr, start, mid - 1, target)

for q in query:
    if binary_search(data, 0, len(data) - 1, q):
        print("yes ")
    else:
        print("no ")

# 13m