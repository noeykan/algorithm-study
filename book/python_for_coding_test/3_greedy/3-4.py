import math

N, K = map(int, input().split())

_, remainder = divmod(N, K)
answer = remainder + int(math.log(N - remainder, K))
print(answer)