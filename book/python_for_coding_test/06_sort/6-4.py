# 퀵소트
# 처음 푼 것
def qsort(arr, start, end):
    if start == end:
        return
    base = start
    left = start + 1
    right = end
    while True:
        while left <= end:
            if array[left] >= array[base]:
                break
            else:
                left += 1
        while right >= start + 1:
            if array[right] <= array[base]:
                break
            else:
                right -= 1
        if left >= right:
            arr[start], arr[right] = arr[right], arr[start]
            base = right
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    if base > start:
        qsort(arr, start, base - 1)
    if base < end:
        qsort(arr, base + 1, end)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
qsort(array, 0, len(array) - 1)
print(array)

# 답지 풀이 - 최적화 된 코드
def qsort(arr, start, end):
    # 이 조건으로 인해서 내가 풀 때보다 아래 qsort를 실행할 때에 if문이 없어도 되어서 더 깔끔함
    if start >= end:
        return
    pivot = start # 공식 명칭은 base라고 하기 보다 pivot이라고 하는게 맞겠다
    left = start + 1
    right = end
    while left <= right:    # if 문에서 break 하는 대신에 이걸로 대신
        while left <= end and array[left] <= array[pivot]: # 이렇게 while 안에 같이 조건으로 묶어버리면 더 깔끔~
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
            pivot = right
        else:
            arr[left], arr[right] = arr[right], arr[left]
    qsort(arr, start, pivot - 1)
    qsort(arr, pivot + 1, end)


# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
qsort(array, 0, len(array) - 1)
print(array)