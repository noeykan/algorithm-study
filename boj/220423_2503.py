# https://www.acmicpc.net/problem/2503
# 숫자 야구

from itertools import permutations

n = int(input())

nums = list(permutations([x for x in range(1, 10)], 3))
valid = [True] * len(nums)

def get_sb(target):


for _ in range(n):
