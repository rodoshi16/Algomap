def jump_game(nums: list[int]) -> bool:
    """

    >>> jump_game([2, 5, 0, 0])
    True
    >>> jump_game([2,3,1,1,4])
    True
    >>> jump_game([2, 0])
    True

    """

    i = len(nums) - 1
    goal = i

    while i > -1:
        if i + nums[i] >= goal:
            goal = i

        i -= 1

    return goal == 0







