# 251203

n = int(input())
data = list(map(int, input().split()))

data.sort()
member_cnt = 0
group_cnt = 0

for d in data:
    member_cnt += 1
    if d == member_cnt:
        group_cnt += 1
        member_cnt = 0

print(group_cnt)

# 30m
# 별것도 아닌데 오래 걸렸음;;