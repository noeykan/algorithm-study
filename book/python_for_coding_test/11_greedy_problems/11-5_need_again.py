N, M = map(int, input().split())
balls = list(map(int, input().split()))
cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        if balls[i] != balls[j]:
            cnt += 1
print(cnt)

# 10분
# O(N^2)
# 1. cnt++ 이런 후위연산자는 파이썬에서 지원하지 않는데 이걸 실수로 썼는데 에러가 안나서 몰랐고, cnt 값이 0으로만 나와서 당황스러웠음
# 2. 문제는 풀었으나 복잡도가 O(N^2)여서 좋은 방법이 아니었다! 아래 답지와 같은 방법이 O(N)이라서 훨씬 좋은 방법임. 어떻게 이런 생각을 했지?
#    나중에 다시 풀어 보도록 하자

# # 답지 방법
# N, M = map(int, input().split())
# balls = list(map(int, input().split()))
#
# ballsArr = [0] * 11
# for b in balls:
#     ballsArr[b] += 1
#
# cnt = 0
# for b in ballsArr[1:]:
#     N -= b
#     cnt += b * N
# print(cnt)