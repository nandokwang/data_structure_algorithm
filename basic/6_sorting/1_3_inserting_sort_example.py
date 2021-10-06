array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def inserting_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]: # ascending order
            # if array[j] > array[j-1]: # dscending order
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array

print(inserting_sort(array))

