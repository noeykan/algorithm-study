nums = list(map(int, list(input())))
result = nums[0]
for i in range(1, len(nums)):
    if result == 0 or result == 1 or nums[i] == 0 or nums[i] == 1:
        result += nums[i]
    else:
        result *= nums[i]
print(result)

# 10분
# 1. string을 굳이 int list로 바꾸지 않아도 string을 for 문으로 돌면서 int()로 각각 바꿔주면 더 깔끔하다
# 2. if 문을 result <= 1 or nums <= 1 로 하는 게 더 좋았을 뻔 