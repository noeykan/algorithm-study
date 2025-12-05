# 251203

# 30분 고민하다 결국 답지 보고 풀었다...

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for d in data:
    if d <= target:
        target += d
    else:
        break
print(target)