S = input().split('-')
result = 0
for i in S[0].split('+'):
    result += int(i)
for i in S[1:]:
    result -= sum(map(int, (i.split('+'))))
print(result)