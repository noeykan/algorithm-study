# 3. 떡볶이 떡 만들기
import sys

N, M = map(int, input().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

def get_length(arr, height):
    length = 0
    for a in arr:
        length += (a - height if a - height >= 0 else 0)

def binary_search(arr, target):
    start = 0
    end = arr[-1]
    middle = (start + end) // 2
    while start <= end:
        if 