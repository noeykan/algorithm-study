# https://www.acmicpc.net/problem/2503
# 숫자 야구

from itertools import permutations

n = int(input())

nums = list(permutations([x for x in range(1, 10)], 3))
valid = [True] * len(nums)

def get_sb(a, b):
    strikes = 0
    balls = 0
    for ia in range(3):
        for ib in range(3):
            if a[ia] == b[ib]:
                if ia == ib:
                    strikes += 1
                else:
                    balls += 1
    return strikes, balls

for _ in range(n):
    in_num, s, b = input().split()
    in_num = tuple(map(int, list(in_num)))
    s = int(s)
    b = int(b)
    for i in range(len(nums)):
        if valid[i]:
            ss, bb = get_sb(nums[i], in_num)
            if ss != s or bb != b:
                valid[i] = False

print(valid.count(True))