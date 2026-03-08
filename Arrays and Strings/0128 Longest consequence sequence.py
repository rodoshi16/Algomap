def longest(nums: list[int]) -> int:
    """

    >>> longest([0,3,2,5,4,6,1,1])
    7

    """

    if nums == []:
        return 0

    nums.sort()
    left = 0
    right = 1
    count = 1
    m = 1
    i = 1

    while right < len(nums):
        if nums[right] == nums[left] + i:
            count += 1
            right += 1
            i += 1
        elif nums[right] == nums[right-1]:
            right += 1
        else:
            left = right
            right = left + 1
            count = 1
            i = 1
        m = max(m, count)

    return m






