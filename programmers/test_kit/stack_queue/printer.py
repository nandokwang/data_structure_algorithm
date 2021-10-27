# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587



def solution(priorities, location):
    num_prior = len(priorities)

    # dummy = priorities

    # for p in priorities[1:]:
    #     if priorities[0] < p:
    #         dummy[0], dummy[num_prior] = dummy[num_prior], dummy[0]

    count = 0

    if any(priorities[0] < i for i in priorities[1:]):
        priorities.append(priorities.pop(0))
        count += 1
    else:

    
    print(priorities)


    answer = 0
    return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0

solution(priorities, location)