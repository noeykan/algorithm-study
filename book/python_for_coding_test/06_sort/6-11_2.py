#251122

N = int(input())
data = [input().split() for _ in range(N)]
for d in data:
    d[1] = int(d[1])

data_sorted = sorted(data, key=lambda student: student[1])

for d in data_sorted:
    print(d[0], end =' ')