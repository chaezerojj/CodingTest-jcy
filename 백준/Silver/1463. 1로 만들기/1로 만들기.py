N = int(input())
dp = [0] * (N + 1)
for i in range(2, N + 1):
    # 3과 2로 나누어 떨어지지 않음 => 1 빼고 횟수 1 추가
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        # 나누어 떨어지면 2를 나눈 것과 비교하여 둘 중 최솟값 고름
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        # 나누어 떨어지면 3을 나눈 것과 비교하여 둘 중 최솟값 고름
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[N])