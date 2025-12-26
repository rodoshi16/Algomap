# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    """

    >>> solution('011100')
    7

    """

    bits = list(S)
    steps = 0

    while any(b == '1' for b in bits):
        if bits[-1] == '0':
            bits.pop()
        else:
            i = len(bits) - 1
            while i >= 0 and bits[i] == '0':
                bits[i] = '1'
                i -= 1
            if i >= 0:
                bits[i] = '0'
        steps += 1

    return steps
