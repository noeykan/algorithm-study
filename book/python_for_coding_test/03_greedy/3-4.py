import math

N, K = map(int, input().split())

_, remainder = divmod(N, K)
answer = remainder + int(math.log(N - remainder, K))
print(answer)

# 지금 보니, N < K 일때 에러 처리 못함.