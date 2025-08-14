n = int(input())
money = 1000 - n
joi = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in joi:
    cnt += money // i
    money %= i
print(cnt)