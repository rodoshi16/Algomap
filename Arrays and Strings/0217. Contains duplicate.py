def hasDuplicate(self, nums: List[int]) -> bool:
"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

Time complexity: 0(n)
space complexity: 0(n) [the memory the dict can use is upto the size of the array]

The reason why are using a hashset and not a list is because a lookup in a list takes 0(n) time complexity but in a hashset 0(1 

"""
hashset = set()
for num in nums:
    if num not in d:
        hashset.add(num)
    else:
        return True 

return false 
