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

    Time complexity: 0(n)

    - for loop runs max len(str)
    - abcdea len(s)-1 0(n) calls max
    - the while loop doesnt run for every of n

    Total Time complexity: 0(n + n) ~ 0(n)

    Space complexity:
    - sub could store the entire string, 0(n)
    - remember that the amount of memory grows linearly with input size

    To be more precise,
    Time: 0(n) where n = len(s)
    Space: 0(m) where m = number of unique characters,
    worst case m = n where all characters are unique


    """
    #substring, we don't know length
    # sliding window, dynamic

    # s: empty
    # len(1)
    #uppercase, lowercase
    # duplicates

    #abcabbcbb
    # iterate, if duplicate, remove all left until no duplicates, add right
    # set: visited

    if len(s) == 1 or len(s) == 0:
        return len(s)

    left = 0
    l = 0

    visited = set()
    for right in range(len(s)):
        while s[right] in visited:
            visited.remove(s[left])
            left += 1

        visited.add(s[right])
        l = max(l, right-left + 1)

    return l










