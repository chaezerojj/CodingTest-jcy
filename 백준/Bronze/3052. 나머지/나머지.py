nums = []
lst = []
for i in range(10):
    num = int(input())
    nums.append(num)
for num in nums:
    lst.append(num % 42)
cnt = []
for i in lst:
    if i not in cnt:
        cnt.append(i)
print(len(cnt))