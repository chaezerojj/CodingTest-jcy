T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    # 가로 탐색
    for i in range(N):
        cnt = 0   # 연속된 1 개수 세기
        for j in range(N):
            if board[i][j] == 1:
                cnt += 1  # 연속 길이 증가
            else:  # 0일때 (검은 칸일때)
                if cnt == K:  # 만약 지금 연속된 길이 cnt한게 K와 같으면
                    result += 1  # 단어 들어갈 수 있으므로 result +1
                cnt = 0  # 초기화
        if cnt == K:  # 행의 끝도 검사
            result += 1

    # 세로 탐색
    for j in range(N):
        cnt = 0
        for i in range(N):
            if board[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    print(f"#{tc} {result}")
    