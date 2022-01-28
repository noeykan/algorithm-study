# Q23. 국영수

N = int(input())
data = []
for _ in range(N):
    d = input().split()
    data.append((d[0], int(d[1]), int(d[2]), int(d[3])))

data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for d in data:
    print(d[0])

# python에서 여러 조건으로 정렬하는거 본 기억이 있는데 가물가물해서 찾아보고 기억나서 품
# https://www.acmicpc.net/problem/10825