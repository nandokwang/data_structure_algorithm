# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
# 전체 원소 입력 받기

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# array = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19]
n = len(array)
target = 7

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)


# 존 벤틀리 * 의 말에 따르면 제대로 이진 탐색 코드를 작성한 프로그래머는 10 % 내외라 할 정도로 실제 구현은 까다롭다. 코드가 짧으니 이진 탐색을 처음 접한 독자라면, 여러 차례 코드를 입력하며 자연스럽게 외워보자. 이진 탐색은 코딩 테스트에서 단골로 나오는 문제이니 가급적 외우길 권한다.