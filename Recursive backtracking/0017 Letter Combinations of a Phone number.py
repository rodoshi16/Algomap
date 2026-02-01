def letterCombinations(digits: str) -> list[str]:
    """

    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




    Example 1:

    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    Example 2:

    Input: digits = "2"
    Output: ["a","b","c"]


    Constraints:

    1 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].

    >>> letterCombinations("23")
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    Time complexity: 0((4**n)*n)

    - number of levels = len(digits), n levels
    - for each digit, the bottom branch can have at most 4 characters(max mapping of a
    digit), there will be 4*n such bottom branches for n levels


    Space: 0(n*(4**n))

    - output list will grow for the number of outputs you have or the total number of
    items in the bottom branch

    """

    d = {
        "2":"abc","3":"def","4":"ghi","5":"jkl",
        "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
    }

    lst = []

    def backtrack(i, cur):
        if len(cur) == len(digits):
            lst.append(cur)
            return

        for c in d[digits[i]]:
            backtrack(i+1, cur+c)

    if digits:
        backtrack(0, "")

    return lst




