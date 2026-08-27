def solution(n):
    res = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
            res.append(n)
        else:
            n = 3 * n + 1
            res.append(n)
    return res