def topKFrequent(nums: list[int], k: int) -> list[int]:
    """

    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
    Example 1:

    Input: nums = [1,1,1,2,2,3], k = 2

    Output: [1,2]

    Example 2:

    Input: nums = [1], k = 1

    Output: [1]

    Example 3:

    Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

    Output: [1,2]



    Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique

    All cases:
    1. Test base case: when len(nums) == k
    2. When the first elements are the clear winners of frequency
    3. Elements at the end have most frequency
    4. Elements with same frequency
    5. Negative numbers

    >>> topKFrequent([1], 1)
    [1]
    >>> topKFrequent([1,2,3], 3)
    [1, 2, 3]
    >>> topKFrequent([1,1,1,2,2,3], k = 2)
    [1, 2]
    >>> topKFrequent([1,2,1,2,1,2,3,1,3,2], k = 2)
    [2, 1]
    >>> topKFrequent([3,3,3,3,3,3,2,2,2,2,2,2,1,1,1,1,1,1], 3)
    [1, 2, 3]
    >>> topKFrequent([3,3,3,3,3,3,2,2,2,2,2,2,1,1,1,1,1,1], 1)
    [1]
    >>> topKFrequent([3,4,5,6,6,6,1,1,1,1,1,1,1, 9,9], 1)
    [1]
    >>> topKFrequent([-1,-1, -1, -8, -8, -9, 9, -9], 2)
    [-1, -9]



    """
    if len(nums) == k:
        return nums

    d = {}

    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 1
        else:
            d[nums[i]] += 1

    sorted_dict = sorted(d, key=lambda k: d[k])
    return sorted_dict[::-1][:k]


