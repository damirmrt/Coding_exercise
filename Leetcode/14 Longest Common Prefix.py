class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:

        s_empty = ''

        for i in range(len(strs[0])):  # iterate over letters in first word
            for s in strs:  # iterate over words for letter i
                if i == len(s) or s[i] != strs[0][i]:
                    return s_empty
            s_empty += strs[0][i]  # if letter i in each word of strs, then add this letter to result

        return s_empty
