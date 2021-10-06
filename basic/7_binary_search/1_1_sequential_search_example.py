# 순차 탐색

# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)


input_data = [5, 'Dongbin']

n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열
array = ['Hanul', 'Jonggu', 'Dongbin', 'Taeil', 'Sangwook']

print(sequential_search(n, target, array))