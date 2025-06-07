def isSubsequence( s: str, t: str) -> bool:
    """

    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



    Example 1:

    Input: s = "abc", t = "ahbgdc"
    Output: true
    Example 2:

    Input: s = "axc", t = "ahbgdc"
    Output: false


    Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.

    Time complexity = 0(n)
    Space complexity = 0(1)

    """

    i = 0
    n = len(s)
    index = 0

    while i < n:
        if s[i] in t and i <= t.index(s[i]):
            index = t.index(s[i])
            i += 1
        else:
            return False
    return True
