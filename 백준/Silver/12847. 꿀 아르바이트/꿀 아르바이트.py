n, m = map(int, input().split())
n_lst = list(map(int, input().split()))

window = sum(n_lst[:m])
max_v = window
max_idx = 0

for i in range(len(n_lst) - m):
    window -= n_lst[i]
    window += n_lst[i + m]
    if window > max_v:
        max_v = window
print(max_v)