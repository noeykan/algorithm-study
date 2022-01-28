# 파이썬의 장점을 살린 quicksort
def qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return qsort(left_side) + [pivot] + qsort(right_side)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
new_arr = qsort(array)
print(new_arr)