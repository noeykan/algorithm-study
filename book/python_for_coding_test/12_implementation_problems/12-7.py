from itertools import combinations

def dist(loc1, loc2):
    return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])

N, M = map(int, input().split())
city_map = [list(map(int, input().split())) for r in range(N)]

houses = []
chicken_shops = []
for r in range(N):
    for c in range(N):
        value = city_map[r][c]
        if value == 1:
            houses.append([r, c])
        elif value == 2:
            chicken_shops.append([r, c])

chicken_combi = list(combinations(chicken_shops, M))
min_city_dist = 2*(N-1)*len(houses)
for chicken_pairs in chicken_combi:
    city_dist = 0
    for h in houses:
        min_dist = 2*(N-1)
        for c in chicken_pairs:
            min_dist = min(min_dist, dist(h, c))
        city_dist += min_dist
    min_city_dist = min(min_city_dist, city_dist)

print(min_city_dist)

# 25분 소요 (40분 제한)

# 백준에서도 답 맞다고 나옴
# https://www.acmicpc.net/problem/15686

