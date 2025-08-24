nums = []
for i in range(9):
    num = int(input())
    nums.append(num)
max_idx = nums.index(max(nums)) + 1
max_v = max(nums)
print(max_v)
print(max_idx)