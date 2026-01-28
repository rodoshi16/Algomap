def binary_search(nums: list[int], target) -> int:
    """
    Given an array of integers nums which is sorted in ascending order, and an
    integer target, write a function to search target in nums. If target exists,
    then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.



    Example 1:

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4
    Example 2:

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

    >>> binary_search([-1,0,2,4,6,8], 3)
    -1
    >>> binary_search([-1,0,2,4,6,8], -1)
    0
    >>> binary_search([-1,0,2,4,6,8], 8)
    5
    >>> binary_search([1,1,1,1], 1)
    1
    >>> binary_search([-7, -6, -5, -2, -1], -1)
    4
    >>> binary_search([-7, -6, -5, -2, -1], -7)
    0
    >>> binary_search([9909090, 797976567, 675767863456], 8)
    -1
    >>> binary_search([], 3)
    -1
    >>> binary_search([3], 3)
    0
    >>> binary_search([3], 5)
    -1
    >>> binary_search([1, 5], 1)
    0
    >>> binary_search([1, 5], 5)
    1


"""

    left = 0
    right = len(nums) -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return - 1


    # l = 0
    # r = len(nums) - 1
    #
    # while l <= r:
    #     mid = (l + r) // 2
    #     if nums[mid] < target:
    #         l = mid + 1
    #     elif nums[mid] > target:
    #         r = mid - 1
    #     else:
    #         return mid
    # return -1





