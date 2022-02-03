# 27. 정렬된 배열에서 특정 수의 개수 구하기

import sys

N, x = map(int, input().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

# 1) bisect 써서 쉽게 풀기
# from bisect import bisect_left, bisect_right

# 2) bisect 라이브러리 직접 구현하기
def bisect_left(arr, a):
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] < a:
            start = middle + 1
        else:
            result = middle
            end = middle - 1
    if result == -1:
        result = len(arr)
    return result

def bisect_right(arr, a):
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] <= a:
            result = middle
            start = middle + 1
        else:
            end = middle - 1
    if result == -1:
        result = 0
    else:
        result += 1
    return result

left_idx = bisect_left(data, x)
right_idx = bisect_right(data, x)

if left_idx == right_idx:
    print(-1)
else:
    print(right_idx - left_idx)
    
# 시간 오래 걸려서 반례 하나 하나 찾아보며 bisect를 구현 하였지만
# 답지 풀이가 오히려 이해해서 써먹기는 더 쉬울 것 같아서 답지 풀이 구현도 한번 다시 해봤으면 좋겠다