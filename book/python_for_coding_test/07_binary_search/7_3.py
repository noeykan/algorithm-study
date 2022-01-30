# 반복문 버전

array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def bs(arr, target, start, end):
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] < target:
            start = middle + 1
        elif arr[middle] > target:
            end = middle - 1
        else:
            return middle
    return None


result = bs(array, 18, 0, len(array)-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)