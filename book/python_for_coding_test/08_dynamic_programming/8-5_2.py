#251123

X = int(input())

d = [0] * 30001

# d[2] = 1
# d[3] = 1
# d[4] = 2
# d[5] = 1

# for i in range(6, X + 1):
#     n_5 = float('inf')
#     if i % 5 == 0:
#         n_5 = d[i // 5] + 1

#     n_3 = float('inf')
#     if i % 3 == 0:
#         n_3 = d[i // 3] + 1
    
#     n_2 = float('inf')
#     if i % 2 == 0:
#         n_2 = d[i // 2] + 1
    
#     d[i] = min(n_5, n_3, n_2, d[i - 1] + 1)

# print(d[X])

#20m

# 위와 같이 하지 말고 그냥 심플하게 아래처럼 하면 될듯;;
# 답지 보고 다시 푼 풀이

for i in range(2, X + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[X])