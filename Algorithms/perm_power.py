def compose(p, q):
    """

    Compose two permutations p and q on {1,...,k}.
    Returns r = p ∘ q

    """
    k = len(p)
    r = [0] * k
    for i in range(k):
        r[i] = p[q[i] - 1]
    return r


def perm_power(p, q, t):
    """

    Returns True if p = q^t, False otherwise
    p, q: permutations on {1,...,k} as lists of length k
    t: nonnegative integer (in binary or decimal)

    """
    result = 1
    power = q

    while t > 0:
        if t % 2 != 0:
            n_result = compose(result, power)

        power = compose(power, power)
        t = t//2

    return result







    # k = len(p)
    # res = list(range(1, k + 1))
    # base = q.copy()
    #
    # while t > 0:
    #     if t % 2 == 1:
    #         res = compose(res, base)
    #     base = compose(base, base)
    #     t //= 2
    #
    # return res == p
    #
