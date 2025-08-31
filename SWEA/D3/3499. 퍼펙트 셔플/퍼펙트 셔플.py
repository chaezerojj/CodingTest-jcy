T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = input().split()

    mid = (N + 1) // 2
    larr = arr[:mid]
    rarr = arr[mid:]

    ans = []
    while larr and rarr:
        ans.append(larr.pop(0))
        ans.append(rarr.pop(0))

    if larr:
        ans.append(larr.pop())

    print(f'#{tc} {" ".join(ans)}')
