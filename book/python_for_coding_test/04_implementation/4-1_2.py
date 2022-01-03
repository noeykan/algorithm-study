def isValid(row, col, N):
    if 1 <= row <= N and 1 <= col <= N:
        return True
    else:
        return False


N = int(input())
guides = input().split()
loc = [1, 1]

for g in guides:
    if g == 'L':
        if isValid(loc[0], loc[1]-1, N):
            loc[1] -= 1
    elif g == 'R':
        if isValid(loc[0], loc[1]+1, N):
            loc[1] += 1
    elif g == 'U':
        if isValid(loc[0]-1, loc[1], N):
            loc[0] -= 1
    elif g == 'D':
        if isValid(loc[0]+1, loc[1], N):
            loc[0] += 1
    else:
        print("Invalid guides!")
print(f"{loc[0]} {loc[1]}")

# 원리는 같으나, 코드를 dx, dy, move_types 등을 array로 미리 만들어두고 코드를 짜면 더 간결하고 깔끔하게 짤 수 있음