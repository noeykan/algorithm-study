#251122

N, T = map(int, input().split())
data = list(map(int, input().split()))

def binary_search(start, end, target):
    while start <= end:
        mid = int((start + end) / 2)
        if target == data[mid]:
            return mid
        elif target > data[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None

res = binary_search(0, len(data) - 1, T)
if res:
    print(res + 1)
else:
    print("원소가 존재하지 않습니다")