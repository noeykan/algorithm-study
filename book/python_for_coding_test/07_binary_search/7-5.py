# 2. 부품찾기
import sys

N = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(arr, target):
    start = 0
    end = len(arr)
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] < target:
            start = middle + 1
        elif arr[middle] > target:
            end = middle - 1
        else:
            return middle
    return None


data.sort()
for t in targets:
    if binary_search(data, t) is not None:
        print("yes", end=' ')
    else:
        print("no", end=' ')
