# B. 숫자 카드 놀이

# 첫번째 풀이(Brute Force) - 시간초과로 실패

import copy
from itertools import combinations

t = int(input())
for _ in range(t):
    data = list(input())
    for i in range(len(data)):
        if data[i] == '6':
            data[i] = '9'

    max_value = 0
    for n in range(1, len(data)):
        print(f'n = {n}', end='  ')
        cnt = 0
        picked = list(combinations(data, n))
        for p in picked:
            d1 = list(p)
            d2 = copy.deepcopy(data)
            for d in d1:
                d2.remove(d)
            d1.sort(reverse=True)
            d2.sort(reverse=True)
            max_value = max(max_value, int(''.join(d1)) * int(''.join(d2)))
            cnt += 1
        print(cnt)
    print()
    # print(max_value)