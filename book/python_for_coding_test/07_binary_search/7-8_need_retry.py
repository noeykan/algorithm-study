# 3. 떡볶이 떡 만들기
import sys

N, M = map(int, input().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

def get_length(arr, height):
    length = 0
    for a in arr:
        length += (a - height if a - height >= 0 else 0)
    return length

def binary_search(arr, target):
    start = 0
    end = arr[-1]
    while start <= end:
        middle = (start + end) // 2
        # 굳이 get_length를 두번 부르지 않고 변수로 저장하고 비교했으면 더 좋았을 뻔
        if get_length(arr, middle) > target:
            start = middle + 1
            # 여기서 result = middle 했어야 함!!
        elif get_length(arr, middle) < target:
            end = middle - 1
        else:
            return middle
    return start

print(binary_search(data, M))

# 거의 근접했는데 약간 틀렸음. binary_search 함수부분이 살짝 미스났는데 중요 포인트를 놓친거라 ... 다시 풀어봐야 함