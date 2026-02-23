def hasDuplicate(nums: list[int]) -> bool:
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

    Time: 0(n)
    Space: 0(n): worst case no duplicates

    """
    #intuitive approach

    d = {}
    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            return True
    return False

    # notice that values just store numbers, we just need to track duplicates elements, not necessarily the values
    # better to use a hashset where we just store the numbers

    s = set()
    for num in nums:
        if num not in d:
            s.add(num)
        else:
            return True
    return False


