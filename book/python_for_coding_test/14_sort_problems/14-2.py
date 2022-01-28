# Q24. 안테나
import sys

N = int(input())
locations = list(map(int, sys.stdin.readline().split()))

locations.sort()
min_dist = float('inf')
for h in locations:


#
# https://www.acmicpc.net/problem/18310