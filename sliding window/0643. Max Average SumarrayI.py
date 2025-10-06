def findMaxAverage(num, k: int) -> float:
    """
    You are given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
    Example 1:

    # >>> findMaxAverage([1,12,-5,-6,50,3], 4)
    # 12.75000


    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
    Example 2:

    Input: nums = [5], k = 1
    Output: 5.00000


    Constraints:

    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104

    Time compelxity: 0(n)
    Space: 0(1)

    """

    curr_sum = 0
    max_avg = 0
    for i in range(k):
        curr_sum += num[i]

    max_avg = curr_sum / k

    for i in range(k, len(num)):
        curr_sum += num[i]
        curr_sum -= num[i - k]

        avg = curr_sum / k
        max_avg = max(avg, max_avg)

    return max_avg





