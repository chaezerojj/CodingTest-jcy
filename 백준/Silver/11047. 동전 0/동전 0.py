N, K = list(map(int, input().split()))
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

result = 0
for coin in coins:
    if K >= coin:
        result += K // coin
        K %= coin
        if K <= 0: break
print(result)