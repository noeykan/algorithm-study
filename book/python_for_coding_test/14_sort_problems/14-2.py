N = int(input())
data = list(map(int, input().split()))

# 처음 풀어서 틀린 풀이
# def get_dist(array, idx):
#     sum = 0
#     for i in range(len(array)):
#         if i != idx:
#             sum += abs(array[i] - array[idx])
#     return sum

# data.sort()
# avg = sum(data) // N

# result = data[0]
# for i in range(N):
#     if data[i] > avg:
#         result = data[i-1] if get_dist(data, i-1) <= get_dist(data, i) else data[i]
#         break

# print(result)

# 한~~~참 생각 후에 생각 난 풀이
data.sort()
print(data[(N - 1) // 2])

# 시간초과(20분) 했고 처음 풀이 답도 틀렸었음...
# 처음엔 그냥 매 위치마다 거리를 계산해서 최소값을 구할까 하다가 보니 N이 200,000이네..?
# O(N^2)으로 풀면 시간 초과라서 포기하고.. 당연히 이건 그냥 봐도 평균값이 맞다고 생각해서
# 첫번째 풀이처럼 평균값을 구하고 거기에 가장 가까운 인덱스에 위치한 값을 출력했는데 답이 틀림...
#
# 문제가 너무 간단한데 못푸는게 자존심 상해서 엄청(두시간) 고민하다가 문득 아래와 같은 사실을 알아냄...
# [1] 5 7 9
#  1 [5] 7 9
# 윗줄서 아랫줄로 갈 때 5 기준으로 왼쪽을 보면, 거리가 5-1=4 만큼 늘어났고, 오른쪽을 보면 거리가 4*3만큼 줄어들었음
# 아... 5-1 = 4만큼 왼쪽에서 한개 늘고 오른쪽에서 세개 줄었구나..? 그럼 결국 총 4*2만큼 거리가 준거네..?
# 이렇게 따지니까 '값' 기준으로 평균을 내는 게 아니라, '개수' 기준으로 정확히 가운데 있는 게 값이 제일 최소네..?
# 5개 있을 때는 3번째가 최소고, 4개 있을때는 2번째 있는거랑 3번째 있는게 최소네? 헐... 개쉽네.... 이렇게 됨..
# 
# https://www.acmicpc.net/problem/18310
