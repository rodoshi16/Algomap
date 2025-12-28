def productExceptSelf(nums: list[int]):
    """

    Given an integer array nums, return an array answer such that answer[i] is
    equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
    integer.

    You must write an algorithm that runs in O(n) time and without using the
    division operation.


    >>> productExceptSelf([1, 2, 3, 4])
    [24, 12, 8, 6]
    >>> productExceptSelf([-1, 1, 0, -3, 3])
    [0, 0, 9, 0, 0]

    Time complexity: 0(n)
    Space complexity: 0(n)




    """
    prefix = [nums[0]]
    suffix = [nums[-1]]

    for i in range(1, len(nums)):
        prefix.append(prefix[-1]* nums[i])

    for i in range(len(nums) -2, -1, -1):
        suffix.insert(0, suffix[0]*nums[i])

    lst = [suffix[1]]

    for i in range(1, len(nums) -1):
        lst.append(prefix[i-1]* suffix[i+1])

    lst.append(prefix[-2])

    return lst

