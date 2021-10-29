# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583


# def solution(bridge_length, weight, truck_weights):
#     num_trucks = len(truck_weights)
#     crossing = [0] * bridge_length
#     dummy_crossing= []
#     count = 0

#     while truck_weights or sum(crossing) != 0:

#         if len(truck_weights) == 0:
#             pass
#         else:
#             if (sum(crossing[1:]) + truck_weights[0]) <= weight:
#                 crossing.append(truck_weights.pop(0))

#         crossing.pop(0)
#         if len(crossing) < bridge_length:
#             crossing.append(0)
    
#         count += 1

#         # print('다건넌 트럭', crossed)
#         print('다리에 있는 트럭', crossing)
#         print('대기 트럭', truck_weights)
#         print('시간', count)
#         print('\n')

#     return count



def solution(bridge_length, weight, truck_weights):
    num_trucks = len(truck_weights)
    crossing = [0] * bridge_length
    dummy_crossing= []
    crossed = []
    count = 0

    while len(crossed) != num_trucks:

        if len(truck_weights) == 0:
            pass
        else:
            if (sum(crossing[1:]) + truck_weights[0]) <= weight:
                crossing.append(truck_weights.pop(0))

        if crossing[0] == 0:
            crossing.pop(0)
        else:
            crossed.append(crossing.pop(0))
        
        if len(crossing) < bridge_length:
            crossing.append(0)
        
        print('다건넌 트럭', crossed)
        print('다리에 있는 트럭', crossing)
        print('대기 트럭', truck_weights)
        print('시간', count)
        print('\n')

        count += 1


    return count



bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]
# truck_weights = [10,10,10,10,10,10,10,10,10,10]

answer = solution(bridge_length, weight, truck_weights)

print(answer)



