x = int(input())
n = int(input())
total = 0

for i in range(n):
    p, c = map(int, input().split())
    total += (p * c)
if x == total:
    print("Yes")
else:
    print("No")