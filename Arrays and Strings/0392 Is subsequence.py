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

    Edge cases:
    1) empty string is always True
    2) subsequence cannot be greater than the length of the String

    Thought process: We iterate through the string and check if matches the
    character of the substring. If not, simply update the position index.
    Time complexity = 0(n)
    Space complexity = 0(1)

    """
    j = 0
    if s == '':
        return True
    if len(s) > len(t):
        return False

    for i in range(len(t)):
        if t[i] == s[j]:
            if j == len(s) - 1:
                return True
        j += 1
    return False



