def is_in_a_star(y: str, a):
    """

    Decide whether a string y belongs to A*

    Ex: A = {ab, b}
    y = ababbb

    We want to figure out of we can break y into pieces where each piece is in A


    """

    n = len(y)

    bool_list = [False] * (n+1)
    bool_list[0] = True

    for i in range(n):
        for j in range(i, n):
            if y[i:j] in a:
                bool_list[i] = True

            bool_list[i] = False



