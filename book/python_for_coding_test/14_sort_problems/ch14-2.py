N = int(input())
data = list(map(int, input().split()))

# 처음 풀어서 틀린 풀이
# def get_dist(array, idx):
#     sum = 0
#     for i in range(len(array)):
#         if i != idx:
#             sum += abs(array[i] - array[idx])
#     return sum

# data.sort()
# avg = sum(data) // N

# result = data[0]
# for i in range(N):
#     if data[i] >= avg:
#         result = data[i-1] if get_dist(data, i-1) < get_dist(data, i) else data[i]
#         break

# print(result)



# 시간초과(20분) 했고 답도 틀렸음...
