# 27. 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right
import sys

N, x = map(int, input().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

left_idx = bisect_left(data, x)
right_idx = bisect_right(data, x)

if left_idx == right_idx:
    print(-1)
else:
    print(right_idx - left_idx)