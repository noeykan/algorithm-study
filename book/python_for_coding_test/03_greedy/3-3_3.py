# 251120

n, m = map(int, input().split())
highest = 0
while n > 0:
    data = map(int, input().split())
    lowest = sorted(data)[0]
    highest = max(highest, lowest)
    n = n - 1
print(highest)

# 6.5m
# sorted는 O(nlogn)이므로 비효율적, min을 쓰면 O(n)임