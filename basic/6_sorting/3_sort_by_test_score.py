"""
2
홍길동 95
이순신 77
"""

# '이순신 홍길동'

# n = int(input())

# array = []
# for i in range(n):
#     input_data = input().split()
#     array.append((input_data[0], int(input_data[1])))

array = [('홍길동', 95), ('이순신', 77)]

# 키(Key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

print(array)