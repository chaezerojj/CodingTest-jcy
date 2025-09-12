def recur(idx, total_height):
    global min_answer
    # 가지치기 : B이상의 높이면 더이상 쌓지 않음
    if total_height >= B:
        min_answer = min(min_answer, total_height)
        return

    if idx == N:  # N명
        return

    recur(idx + 1, total_height + heights[idx])  # 탑에 포함시키는 경우
    recur(idx + 1, total_height)  # 탑에 포함시키지 않는 경우

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    # min_answer = 1e8  # 정답이 보장된 경우는 크게 설정 가능
    min_answer = 10000 * N
    recur(0, 0)
    print(f"#{tc} {min_answer - B}")