def jump_game(nums: list[int]) -> bool:
    """

    >>> jump_game([2, 5, 0, 0])
    True
    >>> jump_game([2,3,1,1,4])
    True
    >>> jump_game([2, 0])
    True

    """

    if nums == [0] or nums == [1]:
        return True

    i = 0
    while i < len(nums)-1:
        if i + nums[i] >= len(nums)-1:
            return True
        elif nums[i] == 0:
            return False
        i += nums[i]

    return False







