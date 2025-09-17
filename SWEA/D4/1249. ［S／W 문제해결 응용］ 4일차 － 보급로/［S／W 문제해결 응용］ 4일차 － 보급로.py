import heapq

def dijkstra():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    distance = [[float('inf')] * N for _ in range(N)]
    distance[0][0] = 0

    pq = [(0, 0, 0)]

    while pq:
        dist, x, y = heapq.heappop(pq)

        if dist > distance[x][y]: continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 > nx or nx >= N or 0 > ny or ny >= N: continue

            cost = dist + MAP[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(pq, (cost, nx, ny))

    return distance[N - 1][N - 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]

    result = dijkstra()
    print(f"#{tc} {result}")