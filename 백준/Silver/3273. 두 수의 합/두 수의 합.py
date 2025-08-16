n = int(input())
n_lst = sorted(list(map(int, input().split())))
x = int(input())
cnt = 0
left = 0
right = n - 1

while left < right:
    if n_lst[left] + n_lst[right] == x:
        cnt += 1
        right -= 1
    elif n_lst[left] + n_lst[right] > x:
        right -= 1
    else:
        left += 1
print(cnt)