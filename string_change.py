def solution(S):
    """

    A string has A, B, C, D

    CBACD -> CBA -> C



    """

    removable = {"AB", "BA", "CD", "DC"}
    changed = True

    while changed:
        changed = False
        i = 0
        new_s = []
        while i < len(S):
            if i + 1 < len(S) and (S[i] + S[i+1] in removable):
                i += 2
                changed = True
            else:
                new_s.append(S[i])
                i += 1
        S = "".join(new_s)
    return S


