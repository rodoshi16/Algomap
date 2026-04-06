def longest(nums: list[int]) -> int:
    """

    >>> longest([0,3,2,5,4,6,1,1])
    7

    """
    #check if the number before exists in arr
    #only start a sequence if n-1 not in set 
    s = set(nums)
    longest = 0

    for n in nums:
        if (n-1) not in s:
            l = 0
            while (n+ l) in n:
                l += 1

            longest = max(l, longest)
    return longest





