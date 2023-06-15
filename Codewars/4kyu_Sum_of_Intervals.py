"""
https://www.codewars.com/kata/52b7ed099cdc285c300001cd

Time Complexity: O(n*logn)
Space Complexity: O(n)
"""

def sum_of_intervals(intervals):
    res = 0
    intervals.sort(key=lambda i: i[0])  # sort according first value in sub-arrays
    combined = [list(intervals[0])]

    for start, end in intervals[1:]:
        lastend = combined[-1][1]  # everytime update lastend

        if start <= lastend:  # if intervals overlap
            combined[-1][1] = max(lastend, end)
            # you need max() here for case [1,5] [2,4]
        else:
            combined.append([start, end])

    for i in range(len(combined)):
        res += combined[i][1] - combined[i][0]

    return res

