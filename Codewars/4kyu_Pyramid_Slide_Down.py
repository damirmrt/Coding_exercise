"""
https://www.codewars.com/kata/551f23362ff852e2ab000037

This solution uses simple 1D Dynamic Programing approach

    [3]      dp = [23, 19, 15, 3, 0]
   [7, 4],   dp = [20, 19, 15, 3, 0]
  [2, 4, 6]  dp = [10, 13, 15, 3, 0]
[8, 5, 9, 3] dp = [8, 5, 9, 3, 0]
             dp = [0, 0, 0, 0, 0]

"""


def longest_slide_down(pyramid):
    dp = [0] * (len(pyramid) + 1)  # define array

    for row in pyramid[::-1]:  # iterate bottom - up
        for i in range(len(row)):
            dp[i] = row[i] + max(dp[i], dp[i + 1])
            # for each row choose current value[i] plus row - 1 max neighbor values

    return dp[0]
