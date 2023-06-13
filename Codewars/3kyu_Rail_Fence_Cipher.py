'''
https://www.codewars.com/kata/58c5577d61aefcf3ff000081

Encoder is much easier than decoder. First we iterate over rails(n),
and then over all values in this rail

For decoder, I didn't make solution with same approach as for encoder.
Detailed explanation in comments.

Time Complexity: O(nlogn)
Space Complexity: O(n)

'''

a = 'WECRLTEEEDROSEEEFOAAIVDEN'
n = 5

def encode_rail_fence_cipher(string, n):
    res = ''
    for r in range(n):
        increment = 2 * (n - 1)  # define how pattern repeats
        for i in range(r, len(string), increment):
            res += string[i]
            if r > 0 and r < n - 1 and i + increment - 2 * r < len(string):
                res += string[i + increment - 2 * r]

    return res


def decode_rail_fence_cipher(string, n):
    cycle = list(range(n)) + list(range(n - 2, 0, -1))
    # create cycle - list of consecutive numbers which goes down and up - 1.
    # Example: for n = 5 cycle will be [0, 1, 2, 3, 4, 3, 2, 1]

    rails = cycle * (len(string) // len(cycle) + 1)
    # Define rails which will be equal to len(string) and filled with cycles

    indices = (i for rail, i in sorted(zip(rails, range(len(string))), key=lambda x: x[0]))
    # Assign rails numbers to characters numbers, then sort rails
    # So we got string indexes sorted for fence cipher eg. [0 8 16 24 1 7 9 15 17 23 2 6 10 14 18]

    chars = (char for i, char in sorted(zip(indices, string), key=lambda x: x[0]))
    # Finally we sort it back to obtain original order.
    return "".join(chars)

print(decode_rail_fence_cipher(a,n))
