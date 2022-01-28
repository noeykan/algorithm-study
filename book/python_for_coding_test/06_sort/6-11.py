# 성적이 낮은 순서로 학생 출력하기
N = int(input())
data = []
for _ in range(N):
    name, score = input().split()
    data.append((name, int(score)))

data.sort(key=lambda x: x[1])
for name, score in data:
    print(name, end=' ')
