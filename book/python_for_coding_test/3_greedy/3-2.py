N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

# K가 최대 횟수이므로, 가장 큰수를 K번 더하고 두번째 큰수를 한번만 더하는 걸 주기로 하면 됨
quotient, remainder = divmod(M, (K + 1))
answer = quotient * (nums[0] * K + nums[1]) + remainder * nums[0]
print(answer)