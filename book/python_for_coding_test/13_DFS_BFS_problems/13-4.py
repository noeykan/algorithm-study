def is_right(p):
    balance = 0
    for c in p:
        if c == "(":
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    if balance == 0:
        return True
    else:
        return False

def separate(p):
    if len(p) == 0:
        return ""
    balance = 0
    w_end = 0
    for i, c in enumerate(p):
        if c == "(":
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            w_end = i
            break
    u = p[:i+1]
    v = p[i+1:]
    if is_right(u):
        return u + separate(v)
    else:
        answer = "("
        answer += separate(v)
        answer += ")"
        u = u[1:-1]
        for c in u:
            if c == "(":
                answer += ")"
            else:
                answer += "("
        return answer

def solution(p):
    return separate(p)

# 시간초과(20분)로, 재귀를 어떻게 적용할 지 헤매서 40분 이상 걸린 듯
# 답은 맞았으나 이해하는 데 좀 시간 걸림