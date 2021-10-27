

def solution(phone_book):
    answer = True
    init_num_length = len(phone_book[0])

    for p_num in phone_book[1:]:
        if phone_book[0] == p_num[0:init_num_length]:
            answer = False
            break

    return answer


phone_book = ["119", "97674223", "1195524421"]

print(solution(phone_book))