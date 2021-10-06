array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print('인풋값:', array)

# 1. sorted 활용(set, dictionary도 활용 삽가능)
result = sorted(array)
print('sorted 활용:', result)

# list 클래스 메소드 활용(별도의 리스트를 리턴하지않고 리스트 내부원소 자체가 바뀜)
array.sort()
print('list.sort() 활용:', array)

# sorted()나 sort()를 이용할대는 key 매개변수를 인풋으로 받을수잇음.
# key값으로는 하나의 함수가 들어가야하며 이는 정렬기준이 되야함
# EX)

array = [('빠나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting) # 두번째인덱스의 숫자기준으로 sort
print(result)

"""
1 .정렬 라이브러리로 풀 수 있는 문제 : 단순히 정렬 기법을 알고 있는지 물어보는 문제로 기본 정렬 라이브러리의 사용 방법을 숙지하고 있으면 어렵지 않게 풀 수 있다.
2. 정렬 알고리즘의 원리에 대해서 물어보는 문제 : 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 문제를 풀 수 있다.
3. 더 빠른 정렬이 필요한 문제 : 퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 계수 정렬 등의 다른 정렬 알고리즘을 이용하거나 문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다.
"""