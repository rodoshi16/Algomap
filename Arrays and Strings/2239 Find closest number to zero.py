from math import inf


def find_closest_number(nums: list[int]) -> int:
    """Given an integer array nums of size n, return the number with the value
    closest to 0 in nums. If there are multiple answers, return the number
    with the largest value.

    input -> list[int]
    output -> int
    function -> to find the element that is closest to n
    exception -> if tie, return largest ele

    Constraints:

    1 <= n <= 1000
    -105 <= nums[i] <= 105

    Time complexity: 0(n)
    Space complexity: 0(1)

    Distance, val, ele stored and doesn't grow over time

    """

    # Runtime is 7ms
    distance = inf
    val = 0
    for ele in nums:
        if abs(ele) < distance:
            distance = abs(ele)
            val = ele
        elif abs(ele) == distance:
            val = max(val, ele)
    return val


# 4ms solution, optimal
def find_closest_number2(nums: list[int]) -> int:
    """

    Faster approach.
    1. Observe that the distance is the main metric here.
    We loop through the entire list to find the smallest.
    2. This can be positive/neg, if it is -ve and its positive version is in the array,
    we return that. Otherwise, just return the closest(its already positive).

    Time complexity: 0(n)
    Space complexity: 0(1)

    closest and ele are the only two variables we store and doesn't grow over time.


    """
    # we're allowed to do this, since constraints start at n = 1,
    closest = nums[0]
    for ele in nums:
        if abs(ele) < closest:
            closest = ele

    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest









