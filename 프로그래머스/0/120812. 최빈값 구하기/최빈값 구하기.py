def solution(array):
    dic = {}
    
    for i in array:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    max_count = max(dic.values())
    
    modes = []
    
    for k, v in dic.items():
        if v == max_count:
            modes.append(k)
    if len(modes) > 1:
        return -1
    
    return modes[0]