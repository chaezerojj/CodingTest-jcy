import math
A, B, V = list(map(int, input().split()))
# V미터 나무 막대기
# 달팽이가 하루에 올라갈 수 있는 길이 = (A - B)
# 다 올라간 날은 미끄러지지 않음! (떨어지는 값 없음)
# (V - (A - B)) * x = V  => B 값 고려 못한거
days = math.ceil((V - B) / (A - B))
print(days)