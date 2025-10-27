def mergeAlternately(word1: str, word2: str) -> str:
    """
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
    Return the merged string.

    Time complexity: 0(n+m), where n and m are the lengths of the strings
    Space complexity: 0(1)

    a,b,result, min_val, max_val

    Edge cases: empty string,

    """
    #Runtime 45ms
    a = len(word1)
    b = len(word2)
    result = ''

    if a < b:
        min_val = word1
        max_val = word2
    else:
        max_val = word1
        min_val = word2

    for i in range(len(min_val)):
        result += word1[i]
        result += word2[i]

    result += max_val[len(min_val):]
    return result

def mergeAlternately(word1: str, word2: str) -> str:
    """

    Note that adding characters to strings is a
    linear operation. For ex, to add "z" to "xy", it needs to
    create another string, then add "z". In lists though, append
    is a constant operation.

    Usually, with merging algorithms, we should 2 pointers since
    thats a clean and better approach.

    In this solution, we have pointers for both words, append as we go and switch
    the toggle from word1 to word2. When one of the iterators is equal to the length,
    we check for both and append whatever is remaining.

    Time complexity: 0(n+m)
    Space complexity: 0(n+m)

    The loop runs through each char of both strings once, n = len(word1) and
    m = len(word2)
    We are storing i,j, result, word but notice that the length of the strings we
    store in result depends on the lengths of word1 and word2. Therefore, it is
    0(n+m)


    """
    #Runtime 32ms -> check leetcode for while loop solution without pointers
    i, j = 0, 0
    result = []
    word = 1

    while i < len(word1) and j < len(word2):
        if word == 1:
            result.append(word1[i])
            i += 1
            word = 2
        else:
            result.append(word2[j])
            j += 1
            word = 1

    while i < len(word1):
        result.append(word1[i])
        i += 1

    while j < len(word2):
        result.append(word2[j])
        j += 1

    return ''.join(result)






