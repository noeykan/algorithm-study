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
#
# 답지 풀이는 더 간단하게 풀었는데 나도 이 생각은 안한 건 아닌데
# 이렇게 풀면 답코드는 좀더 깔끔하게 나오지만 매번 count 함수 부를때마다 N번이 반복 실행되어서 속도가 훨씬 더 느리게 된다.
# 내 코드 O(NlogN), 답지 코드 O(NlogN + N*stage개수)
# 맨 아래에 결과를 붙여 넣었지만 최악의 케이스 테스트 22번의 경우
# 내풀이(31.12ms) >>>> 답지풀이(1131.75ms)

# 답지 풀이
# def solution(N, stages):
#     answer = []
#     length = len(stages)

#     # 스테이지 번호를 1부터 N까지 증가시키며
#     for i in range(1, N + 1):
#         # 해당 스테이지에 머물러 있는 사람의 수 계산
#         count = stages.count(i)
        
#         # 실패율 계산
#         if length == 0:
#             fail = 0
#         else:
#             fail = count / length
        
#         # 리스트에 (스테이지 번호, 실패율) 원소 삽입
#         answer.append((i, fail))
#         length -= count

#     # 실패율을 기준으로 각 스테이지를 내림차순 정렬
#     answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
#     # 정렬된 스테이지 번호 반환
#     answer = [i[0] for i in answer]
#     return answer

# 내가 푼 결과
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.22ms, 10.3MB)
# 테스트 3 〉	통과 (2.76ms, 10.6MB)
# 테스트 4 〉	통과 (24.64ms, 11.2MB)
# 테스트 5 〉	통과 (57.97ms, 15.7MB)
# 테스트 6 〉	통과 (0.26ms, 10.4MB)
# 테스트 7 〉	통과 (2.26ms, 10.4MB)
# 테스트 8 〉	통과 (24.28ms, 11.2MB)
# 테스트 9 〉	통과 (55.13ms, 15.7MB)
# 테스트 10 〉	통과 (23.15ms, 11.2MB)
# 테스트 11 〉	통과 (22.91ms, 11.3MB)
# 테스트 12 〉	통과 (34.34ms, 11.9MB)
# 테스트 13 〉	통과 (37.97ms, 12MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (7.57ms, 10.6MB)
# 테스트 16 〉	통과 (6.43ms, 10.4MB)
# 테스트 17 〉	통과 (12.09ms, 10.7MB)
# 테스트 18 〉	통과 (6.77ms, 10.4MB)
# 테스트 19 〉	통과 (1.33ms, 10.3MB)
# 테스트 20 〉	통과 (9.27ms, 10.5MB)
# 테스트 21 〉	통과 (18.68ms, 10.9MB)
# 테스트 22 〉	통과 (31.12ms, 18.4MB)
# 테스트 23 〉	통과 (34.96ms, 12.2MB)
# 테스트 24 〉	통과 (42.01ms, 12.3MB)
# 테스트 25 〉	통과 (0.01ms, 10.3MB)
# 테스트 26 〉	통과 (0.01ms, 10.3MB)
# 테스트 27 〉	통과 (0.01ms, 10.4MB)

# 답지 결과
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.24ms, 10.3MB)
# 테스트 3 〉	통과 (68.56ms, 10.5MB)
# 테스트 4 〉	통과 (350.30ms, 10.8MB)
# 테스트 5 〉	통과 (1381.19ms, 15.1MB)
# 테스트 6 〉	통과 (1.25ms, 10.3MB)
# 테스트 7 〉	통과 (13.34ms, 10.3MB)
# 테스트 8 〉	통과 (343.91ms, 10.9MB)
# 테스트 9 〉	통과 (1379.94ms, 15MB)
# 테스트 10 〉	통과 (137.39ms, 11MB)
# 테스트 11 〉	통과 (349.18ms, 10.9MB)
# 테스트 12 〉	통과 (199.36ms, 11.5MB)
# 테스트 13 〉	통과 (469.59ms, 11.5MB)
# 테스트 14 〉	통과 (0.04ms, 10.3MB)
# 테스트 15 〉	통과 (11.14ms, 10.6MB)
# 테스트 16 〉	통과 (5.11ms, 10.4MB)
# 테스트 17 〉	통과 (14.58ms, 10.7MB)
# 테스트 18 〉	통과 (5.49ms, 10.4MB)
# 테스트 19 〉	통과 (1.24ms, 10.3MB)
# 테스트 20 〉	통과 (9.69ms, 10.4MB)
# 테스트 21 〉	통과 (16.83ms, 10.9MB)
# 테스트 22 〉	통과 (1131.75ms, 18.4MB)
# 테스트 23 〉	통과 (21.84ms, 11.7MB)
# 테스트 24 〉	통과 (61.96ms, 11.6MB)
# 테스트 25 〉	통과 (0.01ms, 10.3MB)
# 테스트 26 〉	통과 (0.01ms, 10.3MB)
# 테스트 27 〉	통과 (0.01ms, 10.2MB)

