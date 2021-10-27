
""" 
1. count() 메쏘드
"""
# 문자열에서 매칭되는 문자나 숫자 갯수를 세줌
my_list = [0, 0, 1, 3, 5]
print(my_list.count(0))
# 2(0이 2개)

my_list = ['asdf', 'asdf', 'asdf', 'qqq', 'ddd']
print(my_list.count('asdf'))
# 3('asdf'가 3개)

"""
2. collections의 Counter 메쏘드
"""
from collections import Counter

# 리스트의 element들이 key 값, 각 element의 frequency를 value값으로 리턴
print(Counter(my_list))
# Counter({'asdf': 3, 'qqq': 1, 'ddd': 1})

"""
3. list.pop(0)
"""

my_list = [1,2,3]
my_list.pop(0)
print(my_list)
