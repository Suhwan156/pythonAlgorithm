"""
리스트를 최소화하는 방법 중 하나
대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화 할 수 있음

- 리스트 컴프리헨션은 2차원 리스트를 초기화할 때 효과적으로 사용될 수 있음
- 특히 N X M 크기의 2차원 리스트를 한번에 초기화 해야 할 때 ㅁ
"""

# 0부터 9까지 수를 포함하는 리스트
array = [i for i in range(10)]

print(array)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

# N X M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

#N X M 크기의 2차원 리스트 초기화 잘못된 방법
array = [[0] * m] * n
print(array)
array[1][1] = 5
print(array)

# 추가, 리스트에서 특정 값 원소 모두 제거하기
a = {1, 2, 2, 3, 4, 5, 5, 6}
rm_set = {1, 2}

result = [i for i in a if i not in rm_set]
print(result)

# 리스트 전환
# split으로 문자구분 이후, 구분된 문자를 map으로 형 변환, list로 변환
data = list(map(int, input().split()))

print(data)

# 변수 3개로만 받아서 3개만 받기, 더 많은 데이터는 에러남
a, b, c = map(int, input().split())
print(a, b, c)