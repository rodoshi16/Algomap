def merge_sort(l):
    """

    >>> merge_sort([5,4,1,7,2,11])
    [1, 2, 4, 5, 7, 11]

    :param l:
    :return:
    """
    n = len(l)
    if n <= 1:
        return l
    else:
        left = merge_sort(l[:n//2]) # Sort the left subarray
        right = merge_sort(l[n//2:]) # Sort the right subarray
        return merge(left, right) # Merge the sorted subarrays

def merge(l1, l2):
    """
    Input: sorted lists: l1, l2
    Output: l, a sorted list of elements from both l1 and l2
    """
    l = []
    while True:
        # If either list is empty, concatenate the other list to the end and return
        if len(l1) == 0:
            return l + l2
        if len(l2) == 0:
            return l + l1

        # Otherwise, both lists are non-empty, so append the smallest element in either list
        if l1[0] <= l2[0]:
            l.append(l1.pop(0)) # pop(0) retrives first element and removes it from the list
        else:
            l.append(l2.pop(0))

