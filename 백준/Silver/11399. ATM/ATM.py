N = int(input())
P_lst = list(map(int, input().split()))

P_lst.sort()
time = 0
add_p = 0

for i in range(N):
    time += P_lst[i]
    add_p += time
print(add_p)