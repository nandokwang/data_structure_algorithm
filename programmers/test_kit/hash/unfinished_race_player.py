from collections import Counter


def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    print(participant)
    answer = participant - completion

    answer = list(answer.keys())[0]

    return answer

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
participant = ["mislav", "stanko", "mislav", "ana"]	
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))