# 피보나치(Fibonacci Function)를 재귀 함수로 구현

def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(5))

# 이방식은 존나 느림 시간복잡도가 O(2^N)이라서 N=30이면 연산횟수가 10억이넘어감