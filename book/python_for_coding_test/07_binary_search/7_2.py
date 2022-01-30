# 재귀함수 버전

array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def bs(arr, target, start, end):
    # 내풀이
    if start >= end:
        if target == arr[start]:
            return start
        else:
            return None
    # 답지에서는 위의 케이스에서 if start > end 의 경우만 return None을 하고 끝이다
    # start == end 인 경우는 사실 middle도 같기 때문에 알아서 밑에서 찾기 때문에 여기서 굳이 예외처리 안해도 되니까 그게 맞는듯
    middle = (start + end) // 2
    if target < arr[middle]:
        return bs(arr, target, start, middle - 1)
    elif target > arr[middle]:
        return bs(arr, target, middle + 1, end)
    else:
        return middle

result = bs(array, 9, 0, len(array)-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)