#251122

N, T = map(int, input().split())
data = list(map(int, input().split()))

def binary_search(start, end, target):
    if start > end:
        return None
    
    mid = int((start + end) / 2)
    if target == data[mid]:
        return mid
    elif target > data[mid]:
        return binary_search(mid + 1, end, target)
    else:
        return binary_search(start, mid - 1, target)

res = binary_search(0, len(data) - 1, T)
if res:
    print(res + 1)
else:
    print("원소가 존재하지 않습니다")