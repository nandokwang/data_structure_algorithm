# n = 2
# m = 15
# array = [2, 3] # 정답: 5


n = 3
m = 4
array = [3, 5, 7] # 정답 -1



# # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])



# 이 문제는 그리디에서 다루었던 거스름돈 문제와 거의 동일하다. 단지 화폐 단위에서 큰 단위가 작은 단위의 배수가 아니라는 점만 다르다. 그렇기 때문에 그리디 알고리즘을 사용했던 예시처럼 매번 가장 큰 화폐 단위부터 처리하는 방법으로는 해결할 수 없고 다이나믹 프로그래밍을 이용해야 한다.
# -> ??? sort하면 끝나는거아님? ㅈㄴ 어이없네

# count = 0
# array = sorted(array, reverse=True)

# for arr in array:
#     if m // arr != 0:
#         count += m // arr
#         m %= arr

# if count != 0:
#     print(-1)
# else:
#     print(count)
