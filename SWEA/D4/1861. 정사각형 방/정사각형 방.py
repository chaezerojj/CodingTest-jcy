T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)  # 1번 ~ N^2번 방 번호

    # 현재 위치의 숫자 기준으로 상하좌우 확인
    # - 만약 1 큰게 있으면 visited에 1이라고 표시
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny >= N or nx < 0 or nx >= N: continue

                if arr[ny][nx] == arr[y][x] + 1:
                    # 현재 숫자는 다음으로 이동 가능
                    visited[arr[y][x]] = 1
                    break  # 다른 방향은 볼 필요 X
    # print(visited)

    # 연속된 1의 개수가 가장 긴 곳 찾기
    max_cnt = 0  # 정답
    cnt = 0   # 하나하나마다 몇개 연속되는지 확인
    start = 0 # 숫자 카운트한 위치
    for i in range(1, N * N + 1):
        if visited[i] == 1:
            cnt += 1
        else:  # 0을 만나면 계산하기
            if max_cnt < cnt:
                max_cnt = cnt  # 최대값
                start = i - cnt
            cnt = 0
    print(f"#{tc} {start} {max_cnt + 1}")