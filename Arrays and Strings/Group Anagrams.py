from collections import defaultdict
def groupAnagrams(strs: list[str]):
    """
    >>> groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
    [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]


    Time:

    - for loop runs for every char in all strings
    - n: len(strs), k: max length of longest word
    - 0(n*k)

    Space:

    - sig: 0(26) = 0(1)
    - d: worst case all sig are diff len(strs) keys 0(n)
    - values: 0(n*k)

    Total: 0(n) + 0(n*k) ~ 0(n*K)

    """

    #optimal

    d = defaultdict(list)
    for s in strs:
        sig = [0] * 26

        for c in s:
            sig[ord(c) - ord("a")] += 1

        d[tuple(sig)].append(s)

    return list(d.values())

    #brute force
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






