def solution(order):
    answer = 0
    list = ['3', '6', '9']
    order = str(order)
    for i in order:
        if i in list:
            answer += 1
    return answer