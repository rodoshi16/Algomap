def permute(nums: list[int]):
    """

    Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.

    Example 1:

    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    Example 2:

    Input: nums = [0,1]
    Output: [[0,1],[1,0]]
    Example 3:

    Input: nums = [1]
    Output: [[1]]


    """
    l = []
    if len(nums) == 1:
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)

        perm = permute(nums)
        for p in perm:
            p.append(n)
        l.extend(perm)
        nums.append(n)

    return l




