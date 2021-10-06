array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

def count_sort(array):
    sorted_list = []
    count = [0] * (max(array)+1)
    for i in range(len(array)):
        count[array[i]] += 1 # 각데이터에 해당하는 인덱스의 값 증가

    for i in range(len(count)):
        for j in range(count[i]):
            sorted_list.append(i)
    return sorted_list

print(count_sort(array))