def check_structure(n, pillars, floors):
    # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
    for x, y in pillars:
        if y == 0 or (x - 1, y) in floors or (x, y) in floors or (x, y - 1) in pillars:
            pass
        else:
            return False

    # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
    for x, y in floors:
        if (x, y - 1) in pillars or (x + 1, y - 1) in pillars or ((x - 1, y) in floors and (x + 1, y) in floors):
            pass
        else:
            return False

    return True


def solution(n, build_frame):
    pillars = set()
    floors = set()

    for x, y, a, b in build_frame:
        if a == 0:  # 기둥
            if b == 0:  # 삭제
                pillars.remove((x, y))
                if not check_structure(n, pillars, floors):
                    pillars.add((x, y))
            elif b == 1:  # 설치
                pillars.add((x, y))
                if not check_structure(n, pillars, floors):
                    pillars.remove((x, y))
            else:
                print("invalid b value of build_frame when a == 0")
        elif a == 1:  # 보
            if b == 0:  # 삭제
                floors.remove((x, y))
                if not check_structure(n, pillars, floors):
                    floors.add((x, y))
            elif b == 1:  # 설치
                floors.add((x, y))
                if not check_structure(n, pillars, floors):
                    floors.remove((x, y))
            else:
                print("invalid b value of build_frame when a == 1")
        else:
            print("invalid a value of build_frame")

    pillars_res = [[x, y, 0] for (x, y) in pillars]
    floors_res = [[x, y, 1] for (x, y) in floors]
    answer = pillars_res + floors_res
    answer.sort()

    return answer

# 딱 50분에 맞게 풀었음!!
# 처음에 tc가 실패가 뜨길래 공책에 그려서 해보니 check 하는 부분에 실수가 있었음
# 답지를 보니 내가 괜히 set을 썼다고 생각이 듦. 그냥 build_frame 자체에서 pillars와 floors를 구분할 수 있었음. 코드가 훨씬 더 깔끔해짐.

# 아래에서 모두 정답 뜸
# https://programmers.co.kr/learn/courses/30/lessons/60061

