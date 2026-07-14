def solution(nums):
    """

    In an array, a t shift operation takes the elements from end of array to the beginning.
    t = 0, cyclic 0 shift will be [nums[0], nums[1], nums[2].. nums[n-1]]

    t = 1, [num[n-1], nums[0], nums[1], nums[2], ..nums[n-2]]

    t = n-1, [nums[1], nums[2], ...nums[n-1], nums[0]]
    Given an array, find such t such that t shift operations turn nums into a reverse sorted array [n, n-1, ...1]. If there
    is no such t, return -1.

    """
    #find t such that I get I can get the reversed array
    # at every point -> t shifts and check if reversed







