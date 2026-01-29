def checkInclusion(self, s1: str, s2: str) -> bool:
    """

    edge cases:
    - s1, s2 cant be empty
    - no not alphanumeric char

    - "c", "abhchj"
    - "gyghjkhf", "c"
    - "ab", "abgyhfksdhjf"
    - "ab", "gfyrkghjfbgkhab"
    - "ab", "ghfjhgbafyrdghjhr"

    PATTERN: SLIDING WINDOW (FIXED SIZE)

    - looking for substring
    - size of window = len(s1)


    """


    #window size: len(s1)
    # empty: no, at least 1
    # s1 in s2, if s1 >
    # not alphanum -> no

    if len(s1) > len(s2):
        return False

    d = {}
    e = {}
    for ele in s1:
        d[ele] = d.get(ele, 0) + 1


    left = 0
    for right in range(len(s2)):
        e[s2[right]] = e.get(s2[right], 0) + 1


        if right - left + 1 > len(s1):
            e[s2[left]] -= 1
            if e[s2[left]] == 0:
                del e[s2[left]]
            left += 1

        if right - left + 1 == len(s1):
            if  d == e:
                return True

    return False












