# Leet code problem 27 Remove Element
# Given an integer array nums and an integer val, 
# remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.

def removeElementSlim(nums,val):
    ret = nums.count(val) # count the number of values
    while val in nums:
        nums.remove(val) # would only remove it, does not give number of items removed
    return ret

def removeElementLoop(nums,val):
    ret = 0
    for ix in range(len(nums)-1,-1,-1):
        if nums[ix] == val:
            nums.pop(ix)
            ret += 1
    return ret

# removeElement = removeElementSlim
removeElement = removeElementLoop

nums = [3,2,2,3]
val = 3
print(f'before nums is {nums}')
result = removeElement(nums, val)
print(f'after nums is {nums}')
print(f'with val as {val} result is {result}')

nums = [0,1,2,2,3,0,4,2]
val = 2
print(f'before nums is {nums}')
result = removeElement(nums, val)
print(f'after nums is {nums}')
print(f'with val as {val} result is {result}')
