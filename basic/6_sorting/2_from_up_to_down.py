# 인풋예시
"""
3
15
27
12
"""
# 아웃풋예시
'27 15 12'


# N을 입력받기
# n = int(input())

# array = []
# for i in range(n):
#     array.append(int(input()))

array = [3, 15, 27, 12]

# 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

print(array)