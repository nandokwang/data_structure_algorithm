# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587



def solution(priorities, location):
    num_prior = len(priorities)

    if num_prior == 1:
        answer = 1
        return answer
    else:
        count = 0
        idx = [i for i in range(num_prior)]

        while True:
            if idx[0] == location:
                if priorities[0] != max(priorities):
                    pass
                else:
                    break
            
            if priorities[0] != max(priorities):
                priorities.append(priorities.pop(0))
                idx.append(idx.pop(0))
            else:
                priorities.pop(0)
                idx.pop(0)
                count += 1

        answer = count + 1
        return answer


# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
# priorities = [2, 1, 3, 2]
# location = 2
# priorities = [1, 2, 3]
# location = 0
priorities = [1,1,1]
location = 0


answer = solution(priorities, location)

print('답', answer)