'''
A string can be abbreviated by replacing groups of characters with the count of those characters. For example, the word "internationalization" can be abbreviated to "i18n" (where 18 stands for the 18 characters between "i" and "n").
Given a non-empty string word and an abbr (abbreviation), return whether the abbr is a valid abbreviation of word.
Rules:

    The abbreviation string abbr may contain letters and numbers.
    A number in abbr represents the count of characters that are abbreviated.
    A number cannot have leading zeros (e.g., "01" is not valid).
    Letters in abbr must match the corresponding letters in word.

assert validWordAbbreviation("internationalization", "i18n") == True
assert validWordAbbreviation("apple", "a2e") == False
assert validWordAbbreviation("substitution", "s10n") == True
'''
'''
Two pointers, если мы встречаем число считываем его полностью и прибавляем к поинтеру в слове, и далее проверяем матчаться ли буквы
'''

def valid(a,b):
    l = r = 0
  
    while l < len(a) and r < len(b):
        if b[r].isdigit():

            if b[r] == '0':
                return False 
            
            curr_len = 0

            while r < len(b) and b[r].isdigit():
                curr_len = curr_len * 10 + int(b[r])

                r += 1

            l += curr_len

        else:
            if l < len(a) and b[r] != a[l]:
                return False
        
        l += 1
        r += 1

    return True