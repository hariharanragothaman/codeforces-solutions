n = int(input())
nums = input().split()
nums = [int(c) for c in nums]
nums = sorted(nums)
print(nums)

i = 0
if n % 2 != 0:
    print(nums[n//2])
else:
    print(nums[n//2 -1])