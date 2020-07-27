nums = input().split()
nums = [int(c) for c in nums]
nums = sorted(nums)
print(nums[-1]-nums[0])