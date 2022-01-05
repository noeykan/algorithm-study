import copy

def rotate(key):
    return [[key[i][j] for i in range(len(key)-1, -1, -1)] for j in range(len(key))]

def unlock(key, lock):
    M = len(key)
    N = len(lock)
    unlocked = [[1]*N for _ in range(N)]
    for di in range(-M+1, N):
        for dj in range(-M+1, N):
            lock_res = copy.deepcopy(lock)
            for i in range(M):
                for j in range(M):
                    if 0 <= (i + di) < N and 0 <= (j + dj) < N:
                        lock_res[i + di][j + dj] += key[i][j]
            if lock_res == unlocked:
                return True
    return False

def solution(key, lock):
    answer = False
    key_rotated = key
    for _ in range(4):
        if unlock(key_rotated, lock):
            answer = True
            break
        else:
            key_rotated = rotate(key_rotated)
    return answer

# 시간초과(40분)하여 거의 디버깅까지 하면 2시간 넘게 푼듯...;;
# 프로그래머스에서 tc는 모두 맞았음
# https://programmers.co.kr/learn/courses/30/lessons/60059

# 답지를 보니 답지는 나처럼 안하고, 아예 matrix 크기를 늘려서 lock이 한가운데에 있도록 하였음. 이러면 좀 더 코딩이 편할 것 같긴 함
# 난 lock을 매번 deepcopy를 해서 썼는데 답지는 lock에서 key를 다시 빼는 형식으로 계속 lock을 활용하였음