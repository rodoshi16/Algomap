def minEatingSpeed(piles: list[int], h: int) -> int:
    """

    Koko loves to eat bananas. There are n piles of bananas, the ith pile has
    piles[i] bananas. The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she
    chooses some pile of bananas and eats k bananas from that pile. If the pile
    has less than k bananas, she eats all of them instead and will not eat any
    more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas
    before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h
    hours.

    >>> minEatingSpeed([3,6,7,11], 8)
    4

    >>> minEatingSpeed([30,11,23,4,20], 5)
    30

    >>> minEatingSpeed([30,11,23,4,20], 6)
    23

    >>> minEatingSpeed([312884470], 312884469)
    2

    >>> minEatingSpeed([1], 1)
    1

    >>> minEatingSpeed([1, 1, 1, 1], 4)
    1

    >>> minEatingSpeed([9, 9, 9], 3)
    9

    >>> minEatingSpeed([9, 9, 9], 6)
    5

    >>> minEatingSpeed([1000000000, 1000000000], 3)
    666666667

    >>> minEatingSpeed([805306368,805306368,805306368], 1000000000)
    1

    >>> minEatingSpeed([1,2,3,4,5,6,7,8,9], 100)
    1


    >>> minEatingSpeed([10**9], 1)
    1000000000

    >>> minEatingSpeed([1, 10**9], 2)
    1000000000

    >>> minEatingSpeed([1, 10**9], 3)
    500000000


    """
    l = 1
    r = max(piles)
    min_k = max(piles)

    while l <= r:
        mid = (l+r) // 2
        hours = 0

        for ele in piles:
            hours += math.ceil(ele/mid)

        if hours <= h:
            min_k = min(min_k, mid)
            r = mid - 1
        else:
            l = mid + 1

    return min_k




