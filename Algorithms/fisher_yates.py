import random


def fisher_yates(l: list):
    """

    Implement fisher yates algorithm on the list l

    """

    for i in range(len(l)-1, 0, -1):
        r = random.randint(0, i)
        l[i], l[r] = l[r], l[i]

    return l

