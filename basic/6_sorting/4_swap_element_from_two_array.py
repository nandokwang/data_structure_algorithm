a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]

a.sort() # A는 오름차순 정렬(작은것 -> 큰것)
b.sort(reverse = True) # B는 내림차순(큰것 -> 작은것)

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소르 교체
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

