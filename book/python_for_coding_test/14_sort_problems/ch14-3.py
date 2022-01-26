def solution(N, stages):
    stages.sort()
    stage_fail_pair = []
    idx = 0
    player_cnt = len(stages)
    for stage in range(1, N + 1):
        cur_cnt = 0
        while idx < len(stages) and stages[idx] == stage:
            cur_cnt += 1
            idx += 1
        if player_cnt != 0:
            stage_fail_pair.append((stage, cur_cnt / player_cnt))
        else:
            stage_fail_pair.append((stage, 0))
        player_cnt -= cur_cnt
    
    stage_fail_pair.sort(key=lambda x: (-x[1], x[0]))
    answer = [x[0] for x in stage_fail_pair]
    return answer

# 시간초과(20분)해서 40분쯤에 푼 듯...
# 처음에 푼 방식은 for 문을 stage로 돌리는게 아니라 stages 배열 자체를 돌리면서 하다보니 중간에 corner case가 많이 나와서
# 실패 케이스가 몇개 발견되었음. 지금처럼 stage를 기준으로 풀어야 누락 되는 stage 없이 잘 계산이 됨
# 마지막에 런타임 에러 몇개가 나서 고민하다 보니 실패율 구할때 분수의 분모가 0이 되는 경우가 발생해서 이를 예외 처리 해 주니 통과함
# 처음부터 이렇게 풀었으면 좋았을걸 아쉽다
# https://programmers.co.kr/learn/courses/30/lessons/42889
