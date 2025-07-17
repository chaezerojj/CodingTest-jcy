# 1부터 10까지의 정수를 항목으로 갖는 리스트
numbers = list(range(1, 11))

# 짝수만을 선택
evens = filter(lambda x: x % 2 == 0, numbers)

# 짝수 제곱
squared = map(lambda x: x ** 2, evens)

result = list(squared)

print(result)