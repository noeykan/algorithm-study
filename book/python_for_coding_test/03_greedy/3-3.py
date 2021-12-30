N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

min_rows = [min(row) for row in cards]
answer = max(min_rows)
print(answer)