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

    >>> longest_substring(" ")
    1
    >>> longest_substring("abcabcbb")
    3
    >>> longest_substring("pwwkew")
    3
    >>> longest_substring("abcabcabc")
    3


    """
    l = 0
    sub = set()
    max_l = 0

    for right in range(len(s)):
        if s[right] not in sub:
            sub.add(s[right])
        else:
            while s[right] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[right])
        max_l = max(max_l, len(sub))

    return max_l





