N = int(input())
fears = list(map(int, input().split()))
fears.sort()
members = 0
groups = 0
for f in fears:
    members += 1
    if f <= members:
        groups += 1
        members = 0
print(members)