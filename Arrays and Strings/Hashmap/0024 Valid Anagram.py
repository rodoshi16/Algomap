def isAnagram(s: str, t: str) -> bool:
    """

    Given two strings s and t, return true if the two strings are anagrams of each other,
    otherwise return false.

    An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

    Example 1:

    Input: s = "racecar", t = "carrace"

    Output: true
    Example 2:

    Input: s = "jar", t = "jam"

    Output: false
    Constraints:

    s and t consist of lowercase English letters

    """

    #this is the intuitive approach but not efficient to sort because O(nlogn+mlogm)
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

    #instead, use a hashmap to count frequency and return if both freq count is the same

    d = {}
    e = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        d[s[i]] = d.get(s[i], 0) + 1
    for i in range(len(t)):
        e[t[i]] = e.get(t[i], 0) + 1

    return d == e
