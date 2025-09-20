def binary_search(l:list, n: int) -> int:
    """Takes a sorted array and returns the index of n in the array.

    [1,2,3,4,5,6]


    """

    def helper(low, high) -> int:
        if low > high:
            return -1

        mid = (low + high) // 2

        if l[mid] == n:
            return mid
        elif l[mid] > n:
            return helper(low, mid - 1)
        else:
            return helper(mid+1, high)

    return helper(0, len(l) - 1)


















    mid = len(l)//2
    #go left
    if l[mid] > n:
        for i in range(mid, len(l)):
            if i == n:
                return i
            binary_search(l[mid:], n)
    # go right
    for i in range(0, mid):
        if i == n:
            return i
        binary_search(l[0:mid], n)





