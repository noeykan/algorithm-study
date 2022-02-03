import sys
import heapq

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))

if len(cards) == 1:
    print(0)
else:
    total_sum = 0
    while len(cards) != 1:
        cur_sum = heapq.heappop(cards) + heapq.heappop(cards)
        total_sum += cur_sum
        heapq.heappush(cards, cur_sum)
    print(total_sum)

# 못풀다가 결국 heapq 쓰는거 힌트 보고 푼 문제
# 처음엔 그냥 정렬해서 차례로 더하면 되는데 왜 답이 틀리지 하고 한참 고민했었는데
# 10 10 10 10 이런 경우의 반례를 생각 못했었는데 백준 게시판 보고 아 이럴수도 있구나 함
# https://www.acmicpc.net/problem/1715
