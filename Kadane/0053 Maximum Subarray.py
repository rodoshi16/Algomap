def maxSubArray(nums):
    """

    Given an integer array nums, find the subarray with the largest sum, and return its sum.



    Example 1:

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.
    Example 2:

    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.
    Example 3:

    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

    Time: 0(n)
    Space: 0(1)

    """
    currSum = nums[0]
    maxSum = nums[0]

    for i in range(1, len(nums)):
        currSum = max(nums[i], nums[i] + currSum)
        maxSum = max(maxSum, currSum)

    return maxSum

    #Brute Force Solution
    # count = nums[0]
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             if sum(nums[i:j+1]) > count:
    #                 count = sum(nums[i:j+1])
    #
    #     return count
    #
