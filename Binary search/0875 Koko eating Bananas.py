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




