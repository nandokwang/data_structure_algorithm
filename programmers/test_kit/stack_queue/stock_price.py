# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

import time


def solution(prices):
    total_sec = len(prices)
    answer = []
    count = 0

    while len(prices) > 0:
        for p in prices[1:]:
            if prices[0] <= p:
                count += 1
            else:
                count += 1
                break
     
        prices.pop(0)
        answer.append(count)
        count = 0
    
    return answer

prices = [1, 2, 3, 2, 3]

answer = solution(prices)



print(answer)


def solution(prices):
    n = len(prices)  # price 배열의 길이를 n에 저장
    answer = [0] * n # 결과물 answer도 같은 길이로 생성(초기화)
    for i in range(n): # n번 반복을 하면서 가격이 떨어지는 것을 확인
        answer[i] = n-i-1 #  i번째 배열에서 남은 길이(초) 동안 가격이 떨어지는 경우를 위해 남은 길이(초) 전부를 넣는다
        for j in range(i+1, n): # i 이후부터 남은 길이 전부를 반복
            if(prices[i] > prices[j]): # i번째가격이 j번째 가격보다 큰 경우(가격이 떨어진 경우)는 
                answer[i] = j-i # 가격이 떨어진 index에서 i를 빼서 i번째 결과물에 입력
                break; # 떨어졌기때문에 내부 for문을 종료
    return answer # 다 저장된 answer를 리턴
