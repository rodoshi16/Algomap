def findAnagrams(s: str, p: str) -> list[str]:
    """

    Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.



    Example 1:

    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    Example 2:

    Input: s = "abab", p = "ab"
    Output: [0,1,2]
    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".


    Constraints:

    1 <= s.length, p.length <= 3 * 104
    s and p consist of lowercase English letters.

    Time: 0(n)
    Space: 0(p) + 0(p) + 0(s) ~ 0(s) since p <= s

    Edge cases for strings:

    - empty strings (both),
    - one empty string



    """
    #anagrams of p -> frequency map
    # iterate through s using sliding window and check the frequency
    #size of window : 3

    if len(p) > len(s):
        return []

    d = {}
    e = {}
    l = []
    left = 0
    for i in range(len(p)):
        d[p[i]] = d.get(p[i], 0) + 1
        e[s[i]] = e.get(s[i], 0) + 1

    if d == e:
        l.append(0)

    for right in range(len(p), len(s)):
        e[s[right]] = e.get(s[right], 0) + 1
        e[s[left]] -= 1
        if e[s[left]] == 0:
            e.pop(s[left])
        left += 1
        if d == e:
            l.append(left)

    return l


