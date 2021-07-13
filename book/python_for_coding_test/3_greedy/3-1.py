N = int(input("N: "))
coins = [500, 100, 50, 10]

current_change = N
min_coin_cnt = 0
for c in coins:
    # 1. 일반적인 방식
    min_coin_cnt += current_change // c
    current_change %= c

    # 2. divmod 사용
    # cnt, current_change = divmod(current_change, c)
    # min_coin_cnt += cnt

    if current_change == 0:
        break

print(f"{min_coin_cnt}")
