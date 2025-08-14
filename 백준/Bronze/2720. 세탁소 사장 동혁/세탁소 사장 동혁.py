T = int(input())
for tc in range(1, T + 1):
    C = int(input())
    Q = C // 25
    D = (C - 25 * Q) // 10
    N = (C - 25 * Q - 10 * D) // 5
    P = C - 25 * Q - 10 * D - 5 * N

    print(Q, D, N, P)