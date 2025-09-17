def find_boss(n):
    if boss[n] == n: return n  # 자기자신이라면 boss
    result = find_boss(boss[n])  # 재귀호출
    boss[n] = result  # 경로압축
    return result


def union(t1, t2):
    # t2의 보스가 t1의 보스 밑으로 들어간다
    a = find_boss(t1)
    b = find_boss(t2)
    if a == b: return False  # 이미 같은 그룹이면 탈락
    boss[b] = a
    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    E = float(input())
    edges = []

    boss = [i for i in range(N)]

    # 구현 1. 비용을 기준으로 오름차순 정렬
    # 두 섬 사이의 거리 계산
    for i in range(N):
        for j in range(i + 1, N):
            dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            cost = E * dist
            edges.append((i, j, cost))

    # 가중치 기준으로 오름차순 정렬하기
    edges.sort(key=lambda x: x[2])

    # 구현 2. 다른그룹이면 그룹맺기
    cnt = 0
    min_cost = 0
    for u, v, w in edges:
        if union(u, v):
            min_cost += w
            cnt += 1

        if cnt == N - 1:
            break
    print(f"#{tc} {min_cost:.0f}")