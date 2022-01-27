"""
N이 1이 될때까지 밑 수행 반복
1. N에서 1을 뺌
2. N을 K로 나눔
위 과정을 최소로 수행하는 방법 >> 나누기를 많이 하면 댐
"""

n, k = map(int, input().split())

result = 0

while True:

    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

    result += (n-1)
    print(result)