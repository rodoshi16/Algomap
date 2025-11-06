import random


def fisher_yates(l: list):
    """

    Implement fisher yates algorithm on the list l

    >>> random.seed(0)
    >>> lst = [1, 2, 3, 4, 5]
    >>> fisher_yates(lst)
    [4, 5, 1, 3, 2]

    >>> random.seed(123)
    >>> fisher_yates([])
    []

    >>> random.seed(99)
    >>> fisher_yates([1])
    [1]


    """

    for i in range(len(l)-1, 0, -1):
        r = random.randint(0, i)
        l[i], l[r] = l[r], l[i]

    return l

