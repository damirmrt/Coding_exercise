""""
https://www.codewars.com/kata/52742f58faf5485cae000b9a

Time Complexity: O(n)
Space Complexity: O(n)

"""
d = {
    'year': 365 * 24 * 60 * 60,
    'day': 24 * 60 * 60,
    'hour': 60 * 60,
    'minute': 60,
    'second': 1,
}


def format_duration(seconds):
    if not seconds:
        return 'now'

    result = []
    for unit, value in d.items():

        count, seconds = divmod(seconds, value)  # returns quotient and remainder as tuple

        if count == 1: result.append(f"{count} {unit}")  # define will time unit be single...
        if count > 1: result.append(f"{count} {unit}s")  # or plural

    if len(result) == 1: return result[0]

    return f'{", ".join(result[:len(result) - 1])} and {result[-1]}'
