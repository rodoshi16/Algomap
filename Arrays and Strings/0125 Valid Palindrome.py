def isPalindrome(self, s: str) -> bool:
    """

    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
    Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
    Example 2:

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
    Example 3:

    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

    """





    #0(n^2) solution -> not interview optimal, why?
    # look at st += c (1 + 2 + 3 --- + n) so 0(n^2) for the whole loop
    # st.lower() is also 0(n) since it scans the whole string
    # strip(): scans from both ends -> 0(n) in worst case
    # st[::-1]: 0(n)

    st = ""
    for c in s:
        if c.isalnum():
            st += c

    return st.lower().strip() == st[::-1].lower().strip()




