"""
곱하기 혹은 더하기 이용하여 수 더하기, 곱셈 제일 큰 값 구하기
"""

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)