# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0

    while len(progresses) > 0:
        # print('')
        # print((progresses[0] + days*speeds[0]) < 100)
        # print(progresses)
        # print('days:',days, 'count:', count)
        # print('\n')
        if (progresses[0] + days*speeds[0]) < 100:
            if count > 0:
                answer.append(count)
                count = 0
            days += 1
        else:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
    
    answer.append(count)

    return answer



progresses = [93, 30, 55]
speeds = [1, 30, 5]
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]

answer = solution(progresses, speeds)

print(answer)