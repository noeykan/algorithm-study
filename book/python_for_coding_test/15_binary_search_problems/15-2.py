# 28. 고정점 찾기
import sys

N = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = N - 1
result = -1
while start <= end:
    middle = (start + end) // 2
    if data[middle] == middle:
        result = middle
        break
    elif data[middle] < middle:
        start = middle + 1
    else:
        end = middle - 1

print(result)