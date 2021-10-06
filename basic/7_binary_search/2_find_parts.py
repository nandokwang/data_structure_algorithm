
# n = 5
# m = 3

existing_parts = [8, 3, 7, 9, 2]
requiring_parts = [5, 7, 9]

class FindParts:
    def __init__(self, existing_parts, requiring_parts):
        self.existing_parts = sorted(existing_parts)
        self.n = len(self.existing_parts)
        self.requiring_parts = requiring_parts
    

    # 이진 탐색(반복문)
    def binary_search(self, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            # 찾은 경우 중간점 인덱스 반환
            if self.existing_parts[mid] == target:
                return mid
            # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            elif self.existing_parts[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return None
    

    def solve_w_binary_search(self):
        for i in self.requiring_parts:
            result = self.binary_search(i, 0, self.n-1)
            if result != None:
                print('yes', end=' ')
            else:
                print('no', end=' ')


    # 계수 정렬
    def solve_w_count_sort(self):
        array = [0] * 1000001

        # 가게에 있는 전체 부품 번호를 입력 받아서 기록
        for i in self.existing_parts:
            array[int(i)] = 1

        for i in self.requiring_parts:
            if array[i] == 1:
                print('yes', end=' ')
            else:
                print('no', end=' ')
    

    # 집합
    def solve_w_set(self):
        # 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
        array = set(self.existing_parts)
        
        # 손님이 확인 요청한 부품 번호를 하나씩 확인
        for i in self.requiring_parts:
            if i in array:
                print('yes', end=' ')
            else:
                print('no', end=' ')


algorithm = FindParts(existing_parts, requiring_parts)

print('Binary Search Version:')
algorithm.solve_w_binary_search()

print('\nCount Sort Version:')
algorithm.solve_w_count_sort()

print('\nSet Version:')
algorithm.solve_w_set()