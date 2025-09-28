d = [-1, 0, 1]

def dfs(r, c):
    # 마지막열에 도착
    if c == C - 1: return True
    for dr in d:
        nr, nc = r + dr, c + 1
        if not (0 <= nr < R and 0 <= nc < C): continue
        if arr[nr][nc] != '.': continue
        arr[nr][nc] = "x"  # 방문처리
        if dfs(nr, nc): return True
    return False

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
result = 0
for i in range(R):
    if dfs(i, 0): result += 1
print(result)