from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

queue = deque()

for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            queue.append((y, x))

while queue:
    y, x = queue.popleft()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < N and 0 <= nx < M:
            if box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                queue.append((ny, nx))

max_day = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        max_day = max(max_day, box[i][j])
print(max_day -1)