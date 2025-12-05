import heapq

# 1. 초기 답지 힌트 보고 풀다 만 풀이
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1

#     q = []
#     for i, t in enumerate(food_times, start=1):
#         heapq.heappush(q, (t, i))
    
#     t_eaten = 0
#     while q:
#         l = len(q)
#         t, i = heapq.heappop(q)
#         t_one = (t - t_eaten) * l
#         if t_one <= k:
#             k -= t_one
#             t_eaten = t
#         else:
#             break
#     return answer

# 답지보고 품;;; 이 생각을 어떻게하냐...;;; 3가지 포인트에서 막혔는데
# 1) Q: array에서 하나의 음식 다 먹으면, 다음 턴에 건너 뛰어야하는데 어떻게 하지? A: 우선순위 큐!
# 2) Q: pop을 했는데 조건이 안되면 다시 push 해야하나? A: 그냥 pop 하기 전에 q[0] 으로 조건 확인가능
# (우선순위 큐는 자동으로 q에 순서에 맞게 정리해놓고 있어서 가장 작은 값은 그냥 맨 처음 원소임)
# 3) Q: 우선순위 큐에 넣어버려서 원래 배열의 순서(음식 순서)를 보존 못했는데, 어떻게 마지막에 순서를 찾지?
#    A: 그래서 순서를 tuple에 같이 넣었잖아... 그 순서 기반으로 한번 정렬하면 됨;

# 2. 아래 답지 보고 다시 푼 풀이

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i, t in enumerate(food_times, start=1):
        heapq.heappush(q, (t, i))
    
    t_prev = 0
    length = len(q)

    while (q[0][0] - t_prev) * length <= k:
        t, i = heapq.heappop(q)
        k -= ((t - t_prev) * length)
        t_prev = t
        length -= 1
    
    q.sort(key=lambda x: x[1])
    return q[k % length][1]