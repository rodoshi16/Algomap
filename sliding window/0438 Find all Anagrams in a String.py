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

    - no empty strings
    - "r", "ghdjh"
    - "ghdjhf", "r"
    - "ab", "abghfkdjhfk"
    - "ab", "baababababab"

    Space:

    - e: len(p) [worst case all are unique] = 26 char 0(26) ~ 0(1)
    - d: len(p) ~0(1)




    """
    if len(p) > len(s):
        return []

    d = {}

    for ele in p:
        d[ele] = d.get(ele, 0) + 1

    e = {}
    left = 0
    lst = []

    for right in range(len(s)):
        e[s[right]] = e.get(s[right], 0) + 1

        if right - left + 1 > len(p):
            e[s[left]] -= 1
            if e[s[left]] == 0:
                del e[s[left]]
            left += 1

        if right - left + 1 == len(p):
            if d == e:
                lst.append(left)
    return lst




