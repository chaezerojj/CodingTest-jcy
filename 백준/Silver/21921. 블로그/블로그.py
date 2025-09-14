N, X = map(int, input().split())
days = list(map(int, input().split()))

window = sum(days[:X])
max_visit = window
max_cnt = 1
for i in range(len(days) - X):
    window -= days[i]
    window += days[i + X]
    if window > max_visit:
        max_visit = window
        max_cnt = 1
    elif window == max_visit:
        max_cnt += 1
if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(max_cnt)