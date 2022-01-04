def solution(s):
    min_len = len(s)
    # 압축 단위는 1부터 len(s)까지
    for n in range(1, len(s) + 1):
        prev = ""
        res = ""
        cnt = -1
        # n 간격으로 띄어진 index들 생성
        for i in range(0, len(s), n):
            cur = s[i:i+n]
            if cur == prev:
                cnt += 1
            else:
                if cnt == 1:
                    res += prev
                elif cnt > 1:
                    res += (str(cnt) + prev)
                prev = cur
                cnt = 1
        # 맨 끝에 처리가 안된 문자열 처리
        if cnt == 1:
            res += prev
        elif cnt > 1:
            res += (str(cnt) + prev)
        if len(res) < min_len:
            min_len = len(res)
    return min_len

# 시간초과(30분)하여 50분 정도 걸림...
# 프로그래머스에서 모든 tc는 통과하였기 때문에 답은 맞았음
# https://programmers.co.kr/learn/courses/30/lessons/60057

# 답지를 보아하니, 굳이 len(s)까지 안해도 len(s)//2 + 1까지만 압축 단위를 생각해도 되네. 반이 넘어가면 압축이 안될테니까!