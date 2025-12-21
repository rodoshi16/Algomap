def longest_substring(s: str) -> int:
    """

    Given a string s, find the length of the longest substring without duplicate characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


    Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

    >>> longest_substring("pwwkew")
    3

    """
    l = 0
    r = len(s) - 1
    res = ""
    max_l = ""

    for i in range(l, len(s)):
        if s[i] not in res:
            res += s[i]
        else:
            if len(res) > len(max_l):
                max_l = res
            l += 1
            res = ""
    if len(res) > len(max_l):
        max_l = res

    return len(max_l)

