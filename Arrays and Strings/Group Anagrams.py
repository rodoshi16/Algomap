def groupAnagrams(strs: list[str]):
    """
    >>> groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
    [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

    """

    i = 0
    l1 = []
    used = []
    while i < len(strs):
        if strs[i] not in used:
            l2 = [strs[i]]
            used.append(strs[i])
            j = i + 1
            while j < len(strs):
                if len(strs[i]) == len(strs[j]) and sorted(strs[i]) == sorted(strs[j]):
                    l2.append(strs[j])
                    used.append(strs[j])
                j += 1
            l1.append(l2)
        i += 1
    return l1






