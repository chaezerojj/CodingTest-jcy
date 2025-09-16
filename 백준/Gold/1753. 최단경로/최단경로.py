import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start_node):
    # 우선순위 큐: (거리, 노드)형태로 저장
    pq = [(0, start_node)]
    dists = [INF] * (V + 1)
    dists[start_node] = 0  # 시작 노드 거리는 0으로 설정하기

    while pq:
        # 가장 가까운 노드 꺼내기
        dist, node = heapq.heappop(pq)
        
        # 이미 더 짧은 거리 방문한 적 있으면 스킵
        if dists[node] < dist:
            continue
        
        # 현재 노드와 연결된 모든 인접 노드 확인
        for next_dist, next_node in graph[node]:
            # 다음 노드로 가는 새로운 거리 계산
            new_dist = dist + next_dist
            
            if dists[next_node] <= new_dist:
                continue
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    # u번 노드에서 v번 노드로 가는 가중치 w인 간선
    graph[u].append((w, v))

# 최단 거리 계산
result = dijkstra(K)

for i in range(1, V + 1):
    if result[i] == INF:
        print("INF")
    else:
        print(result[i])
