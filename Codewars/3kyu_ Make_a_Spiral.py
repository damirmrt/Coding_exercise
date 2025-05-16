"""
https://www.codewars.com/kata/534e01fbbb17187c7e0000c6

Main idea in my solution is using four pointer. One pointer for each side of 2D array.
On first cycle you iterate ove outer edge of array,
then increment/decrement all pointers by 1 and repeat till you reach center.

Time Complexity: O(n * m)
Space Complexity: O(n * m)

"""


def spiralize(size):
    res = [[0] * size for i in range(size)]
    l = 0
    r = size
    t = 0
    b = size

    while t < b:

        for i in range(l, r):
            res[t][i] = 1

        for i in range(t + 1, b):
            res[i][r - 1] = 1

        t += 2
        if l > 0:
            l += 1

        if size / 2 + 1 == b:
            return res
        for i in range(r - 2, l - 1, -1):
            res[b - 1][i] = 1

        for i in range(b - 1, t - 1, -1):
            res[i][l] = 1

        b -= 2
        r -= 2
        l += 1

    return res


