def isValid(s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


    Example 1:

    Input: s = "()"

    Output: true

    Example 2:

    Input: s = "()[]{}"

    Output: true

    Example 3:

    Input: s = "(]"

    Output: false

    Example 4:

    Input: s = "([])"

    Output: true

    Example 5:

    Input: s = "([)]"

    Output: false



    Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

    Time: 0(n) to traverse the array, push and pop take 0(1)
    Space: 0(n) in case there is no closing

    """
    st = []
    d = {"(": ")", "{": "}", "[": "]"}

    for c in s:
        #faster somehow to do d.keys() than search in d
        if c in d.keys():
            st.append(c)
        elif c in d.values():
            if not st:
                return False
            if d[st.pop()] != c:
                return False

    # not st is faster than == []
    return not st





