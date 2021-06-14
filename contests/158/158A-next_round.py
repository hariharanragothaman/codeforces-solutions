n, k = input().split()
k = int(k)
n = int(n)
k = int(k)
nums = input().split()
nums = [int(c) for c in nums]
limit = nums[k-1]
nums = [c for c in nums if c >= limit and c > 0]
print(len(nums))
