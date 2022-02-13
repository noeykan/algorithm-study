# 33. 퇴사

N = int(input())
data = []
for _ in range(N):
    data.append(tuple(map(int, input().split())))

d = [0] * N
for i in range(N):
    duration, pay = data[i]
    if i == 0:
        prev_pay = 0
    else:
        prev_pay = d[i - 1]
    end_day = i + duration - 1
    if end_day < N:
        d[end_day] = max(d[end_day], prev_pay + pay)
    d[i] = max(d[i], d[i - 1])
print(max(d))

# 제한시간(30분)을 초과함
# 예제는 다 맞았으나 백준에서 70프로 넘어서 답이 틀렸다고 나옴.. 결국 틀림
# https://www.acmicpc.net/problem/14501