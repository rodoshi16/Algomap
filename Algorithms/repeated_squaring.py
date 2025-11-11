import math


def modexp(a: int, b: int, p: int) -> int:
    """

    MODEXP = {⟨a, b, c, p⟩| a, b, c, and p are positive binary integers
    such that a^b ≡ c (mod p)}.

    Note that calculating a^b will be exponential time which is extremely inefficient.
    Therefore, we must calculate in polytime.

    >>> modexp(3,5,7)
    5

    """
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % p

        a = (a * a) % p
        b = math.ceil(b/2)

    return result















