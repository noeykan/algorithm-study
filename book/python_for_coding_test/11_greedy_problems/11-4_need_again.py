N = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for c in coins:
    if c > target:
        break
    target += c

print(target)

# 1시간 생각했는데 못품
# 답지 풀이 보고 푼 거라, 나중에 다시 풀어봐야 할듯. 나중에 풀면 다시 기억 안날듯;; 이런 생각을 어떻게 하지 ㅋㅋ