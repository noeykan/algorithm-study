#251123

N, M = map(int, input().split())
data = list(map(int, input().split()))

def get_sum_cut(arr, length):
    sum = 0
    for a in arr:
        if a > length:
            sum += (a - length)
    return sum

def binary_search(arr, start, end, target):
    if start > end:
        return end # 이게 킥인데 (end를 반환해야 최대 값을 구할 수 있음), 이게 실수하기 쉬우므로 그냥 재귀 말고 for문으로 풀어서 최대 result 값 저장하고 있자
    
    mid = (start + end) // 2
    val = get_sum_cut(arr, mid)
    if val == target:
        return mid
    elif val > target:
        return binary_search(arr, mid + 1, end, target)
    else:
        return binary_search(arr, start, mid - 1, target)

max_h = max(data)
min_h = 0

print(binary_search(data, 0, max_h, M))

#20m