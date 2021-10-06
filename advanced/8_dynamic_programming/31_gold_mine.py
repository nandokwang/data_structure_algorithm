input_1 = 2
input_2 = ['3 4', '4 4']
input_3 = ['1 3 3 2 2 1 4 1 0 6 4 7', '1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2']

# 테스트 케이스(Test Case) 입력
for tc, d2, d3 in zip(range(input_1), input_2, input_3):
    # 금광 정보 입력
    n, m = map(int, d2.split())
    array = list(map(int, d3.split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)