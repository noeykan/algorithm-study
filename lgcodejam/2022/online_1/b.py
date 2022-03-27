# B. K번째 최단 경로

import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

T = int(input())

def get_next_nodes(x, digit):
    nodes = []
    for d in range(digit):
        diff = 10 ** d
        if x // diff % 10 != 9:
            nodes.append(x + diff)
        if x // diff % 10 != 0:
            nodes.append(x - diff)
    return nodes

for _ in range(T):
    L, K, x, y = map(int, input().split())

    parent = [[] for _ in range(10 ** L)]
    distance = [INF] * (10 ** L)
    distance[x] = 0
    q = deque([])
    q.append((0, x))

    while q:
        dist, now = q.popleft()
        if now == y:
            continue
        for node in get_next_nodes(now, L):
            if distance[node] == INF:
                distance[node] = dist + 1
                q.append((dist + 1, node))
            if distance[node] == dist + 1:
                parent[node].append(now)

    count = [0] * (10 ** L)
    count[y] = 1
    q.append(y)
    while q:
        now = q.popleft()
        cnt = count[now]
        if now == x:
            continue
        for node in parent[now]:
            if count[node] == 0:
                q.append(node)
            count[node] += cnt

    if K <= count[x]:
        q.append((K, x))
        while q:
            target, now = q.popleft()
            print(str(now).zfill(L), end=' ')
            if now == y:
                continue
            next_nodes = []
            for node in get_next_nodes(now, L):
                if now in parent[node]:
                    next_nodes.append(node)
            next_nodes.sort()
            for node in next_nodes:
                if target <= count[node]:
                    q.append((target, node))
                    break
                else:
                    target -= count[node]
        print()
    else:
        print("NO")

# 진짜 한 네시간 걸린 것 같다... 삽질 엄청 하고...
# 처음에 했을때 1000과 0999를 연결하는 바람에 맨 마지막 tc가 틀리게 나왔었다. 그냥 단순히 값을 빼서 생긴 문제여서 이를 str으로 바꿔서 해결했음
# 그 다음에 시간초과 나와서 count 세는 부분을 노가다로 세는 게 아니라 parent에 맞게 세니까 훨씬 빨라져서 드디어 성공..!
