N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
largest = nums[-1]
largest_2nd = nums[-2]

result = (M // (K + 1)) * (largest * K + largest_2nd) + M % (K+1) * largest
print(result)

# 5분