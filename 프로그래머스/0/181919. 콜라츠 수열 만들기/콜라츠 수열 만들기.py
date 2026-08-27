def solution(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + solution(n//2)
    else:
        return [n] + solution(3 * n + 1)