def maxArea(height: list[int]) -> int:
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    >>> maxArea([1,8,6,2,5,4,8,3,7])
    49
    >>> maxArea([1,1,1,1,1,1,1])
    6
    >>> maxArea([9,1,2])
    4
    >>> maxArea([1, 100])
    1
    >>> maxArea([0, 0, 0, 0])
    0
    >>> maxArea([1000, 1, 1, 1, 1000])
    4000
    >>> maxArea([1, 2, 3, 4, 5])
    6
    >>> maxArea([5, 4, 3, 2, 1])
    6
    >>> maxArea([5, 5, 5, 5, 5])
    20
    >>> maxArea([10000, 10000])
    10000
    >>> maxArea([1, 2, 100, 2, 1])
    4
    >>> maxArea([0, 2, 0, 4, 3])
    6


    """

    l = 0
    r = len(height) - 1
    area = 0

    while l < r:
        w = abs(r-l)
        h = min(height[l], height[r])
        area = max(area, w*h)

        if height[l] < height[r]:
            l += 1
        elif height[r] < height[l]:
            r -= 1
        else:
            l += 1
            r -= 1

    return area

