
def find_duplicates(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Given two lists, return a sorted array of duplicates in both lists.
    arr1 and arr2 might not be the same length, aka: one could be bigger than the
    other

    Clarifying questions:

    - sorted
    - return duplicates arr in sorted order
    - (-ve) numbers




    # n = 1'000'000
    # m = 10

    # 1'000'000 * log (10) = 3'000'000
    # log(1'000'000) * 10 = 20 * 10 = 200
    # O ( n + m) = 1'000'010

    # [1, 2, 3, 4, 5, 6, 7, 8]
    # -10

    # [1, 2, 3, 4, 5, 6, 7, 8, .., 500, .., 1000]
    # 1


    >>> find_duplicates([1, 2, 3], [3, 4, 5, 6])
    [3]

    """

    # it doesn't matter which arr is greater because while condition will be false when one of them goes out of bounds
    # time: 0(n+m)
    #space: 0(1)

    i, j = 0, 0
    lst = []
    while i < len(arr1) and j < len(arr2):

        if arr1[i] == arr2[j]:
            lst.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return lst

    # n = len(small), m = len(large)
    # 0(n*log(m)) solution
    #
    # if len(arr1) < len(arr2):
    #     small, large = arr1, arr2
    # else:
    #     small, large = arr2, arr1
    #
    #
    # lst = []
    # for i in range(len(small)):
    #     left = 0
    #     right = len(large) -1
    #
    #     #check boundary
    #     if large[0] <= small[i] <= large[-1]:
    #         while left <= right:
    #             mid = (left + right)//2
    #             if large[mid] == small[i]:
    #                 lst.append(large[mid])
    #                 break
    #             elif large[mid] < small[i]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    # return lst








