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

    >>> permute([1, 2, 3])
    [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]


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

#given a string returns the longest portion where no char repeat

"abcdefghjikl"
"abcda"
"bbbb"


def f(s: str):
    """

    >>> f("abcdeee")
    5

    babacdef

    """
    left = 0
    st = set()
    max_l = 0
    for right in range( len(s)):
        if s[right] not in st:
            st.add(s[right])
        else:
            while s[right] in st:
                st.remove(s[left])
                left += 1
            st.add(s[right])
        max_l = max(max_l, len(st))

    return max_l





    return

"""

#find increasing subsequence of an array
input -> int 
constraints -> 10^5 

[1, 2, 4, 3, 0] 
empty list -> longest subsequence would be 0 

"""


def long(nums: list[int]):
    """
    >>> long([1, 2, 4, 3, 0])
    [1, 2, 4]




    """
    m = 0
    l = 0
    for right in range(len(nums)):
        while nums[l] > nums[right]:
            l += 1
            m = max(m, len(nums[l: right]))
    return m
















