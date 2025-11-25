# Leet Code Problem 35 Search Insert Position
# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        ret = len(nums)
        for ix, item in enumerate(nums):
            if item > target:
                ret = ix
                break
        return ret

nums = [1,3,5,6]
target = 5
ret = searchInsert(nums,target)
print(f'the result is {ret}')
# Output: 2

nums = [1,3,5,6]
target = 2
ret = searchInsert(nums,target)
print(f'the result is {ret}')
# Output: 1

nums = [1,3,5,6]
target = 7
ret = searchInsert(nums,target)
print(f'the result is {ret}')
# Output: 4