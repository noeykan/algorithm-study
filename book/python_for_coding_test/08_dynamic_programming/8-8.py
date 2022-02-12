# 5. 효율적인 화폐 구성

N, M = map(int, input().split())
pay = [int(input()) for _ in range(N)]

d = [0] * 10001
for p in pay:
    d[p] = 1

def get_min_cnt(n):
    if d[n] == 0:
        min_cnt = 10001
        for p in pay:
            if n - p > 0:
                prev_cnt = get_min_cnt(n - p)
                if prev_cnt == 0:
                    min_cnt = 0
                else:
                    min_cnt = min(min_cnt, preve_cnt + 1)
        d[n] = min_cnt if min_cnt != 10001 else 0
    return d[n]

answer = get_min_cnt(M)
if answer != 0:
    print(answer)
else:
    print(-1)

# 아래 답지 코드가 더 효율적인듯 이해하도록 하자
# # 정수 N, M을 입력 받기
# n, m = map(int, input().split())
# # N개의 화폐 단위 정보를 입력 받기
# array = []
# for i in range(n):
#     array.append(int(input()))
#
# # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
# d = [10001] * (m + 1)
#
# # 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
# d[0] = 0
# for i in range(n):
#     for j in range(array[i], m + 1):
#         if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
#             d[j] = min(d[j], d[j - array[i]] + 1)
#
# # 계산된 결과 출력
# if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
#     print(-1)
# else:
#     print(d[m])