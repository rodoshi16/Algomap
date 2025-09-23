def bubble_sort(l: list) -> list:
    """"

    >>> bubble_sort([2,5,3,8,4,9,1])
    [1, 2, 3, 4, 5, 8, 9]

    Time complexity: 0(n^2)
    Space: 0(1)


    """

    for i in range(len(l) - 1):
        for j in range(len(l) -1 - i):
            if l[j + 1] < l[j]:
                l[j+1], l[j] = l[j], l[j+1]

    return l

