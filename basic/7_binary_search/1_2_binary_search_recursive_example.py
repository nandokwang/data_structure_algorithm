# binary search는 배열 내부의 데이터가 무작위일때는 사용할수없고, 정렬되어 있어야만 사용할수 있는 알고리즘.

# binary search는 위치를 나타내는 변수 3개를 사용함: 시작점, 중간점, 끝점(인덱스기준)
# 중간점 인덱스가 실수일 때는(배열의 길이가 짝수일때) 소수점 이하를 버린다. ex) 중간점이 4.5 면 4를 중간점으로 정함(바닥함수)

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# array = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19]

n = len(array)
target = 7

# 이진 탐색 수행결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않읍니다')
else:
    print(result+1)