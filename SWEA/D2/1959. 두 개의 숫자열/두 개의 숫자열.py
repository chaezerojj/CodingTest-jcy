T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        N, M = M, N
        A, B = B, A
    ans = -1e10
    for i in range(N - M + 1):
        result = 0
        for j in range(M):
            result += A[j + i] * B[j]
        ans = max(ans, result)
    print(f"#{tc} {ans}")