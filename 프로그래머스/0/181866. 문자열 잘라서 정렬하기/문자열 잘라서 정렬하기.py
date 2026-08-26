def solution(myString):
    answer = []
    arr = myString.split("x")
    for i in arr:
        if i not in " ":
            answer.append(i)
    return sorted(answer)