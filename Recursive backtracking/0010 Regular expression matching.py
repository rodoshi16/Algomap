def isMatch(self, s: str, p: str) -> bool:
    """

    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).



    Example 1:

    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    Example 2:

    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    Example 3:

    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".


    Constraints:

    1 <= s.length <= 20
    1 <= p.length <= 20
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.



    """


    pattern = p
    text = s
    if len(pattern) < len(text):
        return False

    p1 = 0
    p2 = 0

    while p1 < len(text) and p2 < len(pattern):
        previous_char = text[p1]
        if  pattern[p2] == '.':
            p1 += 1
        elif pattern[p2] == "*":
            while text[p1] == previous_char:
                p1 += 1
        elif text[p1] != pattern[p2]:
            return False
        else:
            p1 += 1
    return True

