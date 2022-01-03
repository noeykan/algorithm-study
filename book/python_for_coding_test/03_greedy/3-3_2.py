N, M = map(int, input().split())
min_card = 1
for _ in range(N):
    row_cards = list(map(int, input().split()))
    if min(row_cards) > min_card:
        min_card = min(row_cards)
print(min_card)

# 5분