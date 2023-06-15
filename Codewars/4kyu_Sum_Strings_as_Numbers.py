"""
It is kind of ugly bit linear time and space :)

Time Complexity: O(n)
Space Complexity: O(n)

"""

def sum_strings(x, y):
    if not x and not y:  # edgecase
        return '0'
    surplus = 0
    res = ''
    # addign leading zeros to smaller number
    if len(x) > len(y):
        y = y[::-1] + "0" * (len(x) - len(y))
        y = y[::-1]
    elif len(x) < len(y):
        x = x[::-1] + "0" * (len(y) - len(x))
        x = x[::-1]

    for i in range(len(x) - 1, -1, -1):  # add number by number
        tmp = int(x[i]) + int(y[i]) + surplus
        if tmp > 9:
            res += str(tmp % 10)
            surplus = 1
        else:
            res += str(tmp)
            surplus = 0
    if surplus == 1:
        res += "1"
    if res[-1] == "0" and len(res) > 1:
        res = res[:len(res) - 1]
    return res[::-1]

