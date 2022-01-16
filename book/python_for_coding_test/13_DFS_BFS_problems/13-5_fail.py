# 내 풀이 (처참하게 실패)
N = int(input())
numbers = list(map(int, input().split()))
ops_cnt = list(map(int, input().split()))

ops = [-1] * (N - 1)

max_res = float("-inf")
min_res = float("inf")

def dfs(count):
    if count == (N - 1):
        global max_res
        global min_res
        res = numbers[0]
        for n, op in enumerate(ops):
            num = numbers[n + 1]
            if op == 0:  # 덧셈
                res += num
            elif op == 1:  # 뺄셈
                res -= num
            elif op == 2:  # 곱셈
                res *= num
            elif op == 3:  # 나눗셈
                if res < 0:
                    res *= -1
                res = res // num
                if res < 0:
                    res *= -1
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return

    for i in range(4):
        for j in range(ops_cnt[i]):
            for k in range(N-1):
                if ops[k] == -1:
                    ops[k] = i
                    ops_cnt[i] -= 1
                    dfs(count + 1)
                    ops_cnt[i] += 1
                    ops[k] = -1

dfs(0)
print(max_res)
print(min_res)

# 제한시간(30분)을 까마득히 넘기고 고민의 고민을 거듭하고 디버깅을 거듭해서 몇시간 째 풀었는데 답은 나오는데
# 너무 필요 개수 이상으로 돌아서 백준에서는 시간초과가 뜸...
# https://www.acmicpc.net/problem/14888

# 아래는 답지니까 이해 하길 바람... 와 쉽지 않네...

# n = int(input())
# # 연산을 수행하고자 하는 수 리스트
# data = list(map(int, input().split()))
# # 더하기, 빼기, 곱하기, 나누기 연산자 개수
# add, sub, mul, div = map(int, input().split())
#
# # 최솟값과 최댓값 초기화
# min_value = 1e9
# max_value = -1e9
#
# # 깊이 우선 탐색 (DFS) 메서드
# def dfs(i, now):
#     global min_value, max_value, add, sub, mul, div
#     # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
#     if i == n:
#         min_value = min(min_value, now)
#         max_value = max(max_value, now)
#     else:
#         # 각 연산자에 대하여 재귀적으로 수행
#         if add > 0:
#             add -= 1
#             dfs(i + 1, now + data[i])
#             add += 1
#         if sub > 0:
#             sub -= 1
#             dfs(i + 1, now - data[i])
#             sub += 1
#         if mul > 0:
#             mul -= 1
#             dfs(i + 1, now * data[i])
#             mul += 1
#         if div > 0:
#             div -= 1
#             dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
#             div += 1
#
# # DFS 메서드 호출
# dfs(1, data[0])
#
# # 최댓값과 최솟값 차례대로 출력
# print(max_value)
# print(min_value)
