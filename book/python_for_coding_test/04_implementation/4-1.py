N = int(input())
plan = input().split()

location = [1, 1]

for p in plan:
    if p == 'L' and location[1] > 1:
        location[1] -= 1
    elif p == 'R' and location[1] < N:
        location[1] += 1
    elif p == 'U' and location[0] > 1:
        location[0] -= 1
    elif p == 'D' and location[0] < N:
        location[0] += 1

print(*location)
