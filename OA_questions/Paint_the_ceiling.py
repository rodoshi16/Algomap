def paint_the_ceiling(n: int, s: int, k: int, b: int, a: int, m: int) -> int:
    """

    A building company offers houses with sides from a specific set of lengths. They are
    running a promotion: free ceiling painting if the house area is not more than a.

    The company determines its offered side length using a formula:
    s[i] = ((k x s[i-1]+b)mod m) ) + 1 + s[i-1] for 1<=i<=n
    Starting with a seed value s[0] = s0 and parameters k,b,m, they generate n
    total wall lengths.

    Determine how many possible house configurations (rect or square) you can create
    using these side lengths
    while keeping the area less than or equal to a to qualify for free ceiling
    painting.

    s0 = 2
    n = 3
    k = 3
    b = 3
    m = 2
    a = 15

    First, calc the wall lengths, then check all the possible combinations and the ones that are less
    than 15 are valid.

    >>> paint_the_ceiling(3, 2, 3, 3, 15, 2)
    5


    """

    count = 0
    sides = [s]
    for i in range(1, n):
        n = ((k * sides[i-1] + b) % m) + 1 + sides[i-1]
        sides.append(n)

    i = 0
    j = i

    while i < len(sides):
        if sides[i] * sides[j] <= a:
            count += 1
        j += 1
        if j == len(sides):
            i += 1
            j = 0

    return count


