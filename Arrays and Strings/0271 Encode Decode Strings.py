def encodedecode(s: list[str]) -> list[str]:
    """
    Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

    Test cases:
    1. Single char
    2. Spaces
    3. Letter between spaces
    4. Ascii charatcers
    5. Trying dots
    6. Trailing spaces
    7. Numbers
    8. Empty case


    >>> encodedecode(["neet", "code", "love", "you"])
    ['neet', 'code', 'love', 'you']
    >>> encodedecode(["neet", "code", "love", "you"])
    ['neet', 'code', 'love', 'you']

    >>> encodedecode(["a"])
    ['a']

    >>> encodedecode(["hello", ""])
    ['hello', '']

    >>> encodedecode(["", ""])
    ['', '']

    >>> encodedecode(["", "hi", ""])
    ['', 'hi', '']

    >>> encodedecode(["#"])
    ['#']

    >>> encodedecode(["###"])
    ['###']

    >>> encodedecode(["a#b#c"])
    ['a#b#c']

    >>> encodedecode([".", "www.google.com", "neetcode.io"])
    ['.', 'www.google.com', 'neetcode.io']

    >>> encodedecode(["text with spaces", "  leading", "trailing  "])
    ['text with spaces', '  leading', 'trailing  ']

    >>> encodedecode(["123", "00001", "42#life"])
    ['123', '00001', '42#life']

    >>> encodedecode(["10", "#10#", "010"])
    ['10', '#10#', '010']

    >>> encodedecode(["", "42", "", "#", "endend"])
    ['', '42', '', '#', 'endend']

    >>> encodedecode([])
    []





    """
    return decode(encode(s))


def encode(strs: list[str]) -> str:
    si = ""
    for s in strs:
        si += str(len(s)) + "#" + s
    return si


def decode(s: str) -> list[str]:
    lst = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])

        lst.append(s[j+1: j+1+length])
        i = j+1+length
    return lst
