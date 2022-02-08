import sys

N, C = map(int, input().split())
data = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
data.sort()

def get_max_cnt(arr, gap):
    cnt = 1
    loc = arr[0]
    for a in arr[1:]:
        if (a - loc) >= gap:
            cnt += 1
            loc = a
    return cnt

start = 1
end = data[-1] - data[0]

min_gap = end
while start <= end:
    middle = (start + end) // 2
    max_cnt = get_max_cnt(data, middle)
    # ### 처음 풀었을때 틀렸던 코드 ###
    # if max_cnt > C:
    #     start = middle + 1
    # elif max_cnt < C:
    #     end = middle - 1
    # else:
    #     min_gap = middle
    #     start = middle + 1
    ######
    if max_cnt >= C:
        min_gap = middle
        start = middle + 1
    else:
        end = middle - 1

print(min_gap)

# 제한시간(50분) 넘기고 하루이틀 고민하다 답 봤는데 이럴수가 이렇게 간단하다니..;;
# 코드는 안보고 설명만 보고, 직접 코딩 해 봤는데 자꾸 에러 떠서 설마 이건가 하고 고쳤는데 답 맞음
# 처음 풀었을 때 반례를 알고싶은데 잘 모르겠다....가 나랑 같은 질문 한 사람 있어서 알게 됨
# (참고 https://www.acmicpc.net/board/view/74023)
# 반례 input
# 4 3
# 1
# 3
# 5
# 7
# 반례를 하나하나 해보며 겨우 내 처음 풀이가 왜 틀렸었는 지 이해함...!
# https://www.acmicpc.net/problem/2110
