def romanToInt(self, s: str) -> int:
    """
     Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.

    Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

    Thought process: In order to find the values, we cannot just compare individual characters to
    the dict values since IV,IX, CM etc have 2 characters. Therefore, we need to iterate and find
    if the value before our character is less or not.

    Time complexity: 0(n)
    Space complexity: 0(1)

    """
    # if you're bigger than i+1 -> add to result
    # if you're less than i+1 -> subtract value i+1 - i and add that to result,
    # then move two indices since i+1 has been used

    d = {"M": 1000,"D": 500,"C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    result = 0
    n = len(s)
    i = 0

    while i < n:
        if i < n-1 and d[s[i]] < d[s[i+1]]:
            dif = d[s[i+1]] - d[s[i]]
            result += dif
            i += 2
        else:
            result += d[s[i]]
            i += 1
    return result


