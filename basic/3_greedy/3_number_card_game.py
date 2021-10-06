# min() 함수를 이용하는 답안 예시

# N, M을 공백을 기준으로 구분하여 입력 받기 '3 3'
n, m = map(int, input().split())

# 3 1 2
# 4 1 4
# 2 2 2

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)


# ----------------------------------------------------------------------------#
# ----------------------------------------------------------------------------#
# ----------------------------------------------------------------------------#

# 2중 for 문 구조를 이용하는 답안 예시

# N, M을 공백을 기준으로 구분하여 입력 받기 '3 3'
n, m = map(int, input().split())

# 3 1 2
# 4 1 4
# 2 2 2

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)