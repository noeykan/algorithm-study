from collections import deque
import sys

def bfs(graph, min_dist, start, dist_target):
    q = deque([start])

    answer = []
    while q:
        city = q.popleft()
        if min_dist[city] == dist_target:
            answer.append(city)
            continue

        for city_next in graph[city]:
            if min_dist[city_next] != 0:    # 이미 city_next는 방문 된 도시임
                continue
            elif city_next == start:
                continue
            else:
                min_dist[city_next] = min_dist[city] + 1
                q.append(city_next)

    return sorted(answer)

N, M, K, X = map(int, sys.stdin.readline().split())
roads = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

city_graph = [[] for _ in range(N+1)]   # 도시는 1부터 시작
for c1, c2 in roads:
    city_graph[c1].append(c2)

city_dist = [0] * (N + 1)

answer = bfs(city_graph, city_dist, X, K)
if len(answer) == 0:
    print(-1)
else:
    print(*answer, sep="\n")

# 시간초과(30분)으로 계속 오답이 떠서 삽질 하느라 2시간은 쓴 것 같다...
# 삽질원인 분석
# 1. 문제 접근을 처음에 잘못해서 큐에 (city, dist)를 같이 넣고 빼고 했었는데
#    이 얘기는 전체적으로 최소 거리를 관리 하지 않고, 각각 현재 도시로 올 때의 거리만 알기 때문에
#    이 거리가 '최소거리'인지 아닌지 판단할 수가 없었음.
# 2. 최소거리를 관리하는 객체를 만들고 하였는데도 계속 답이 안나와서 백준 게시판 질문 검색 해보니
#    누가 반례를 올려주었는데 1->2->3->1 로 다시 돌아 올때 최소 거리는 0이라는 것....
#    문제에 시작 도시로 가는 최단 거리는 0이라고 써 있는데 이걸 제대로 인지 못한 내 잘못.
# 3. 위 2번이 해결 됐는데도 답이 안풀리길래 삽질 겁나하다가 답을 보니... "오름차순으로 출력한다..."
#    라는 내용이 문제에 있었네.......후...... 입력 출력 조건 하나하나 꼼꼼이 다 봐야 한다는 교훈...
#
# 코드 최적화
# 답지에서는 dist를 -1로 초기화를 한 후에, 출발점 값만 0으로 초기화 하였음
# 이렇게 하면 나처럼 값이 0 이 아닌지 검사하는 것과 시작점이 아닌지 검사하는것 두개가 있을 필요가 없음
# -1 인지만 조사하면 됨..! 멋지네!

# https://www.acmicpc.net/problem/18352
