s = "лилилось и дальше лилилась"

a = 'лилила'


def pref_suf(a):
    p = [0] * len(a) # максимального префикса\суффикса

    j = 0
    i = 1

    while i < len(a):
        if a[j] == a[i]:
            # если текущий и след символ совпадают 
            # добавляем единицу в массив p [0,1]
            p[i] = j+1
            i += 1
            j += 1
            # и двигаем оба указателя
        else: # иначе  если j в начале обнуляем p и двигаем только i
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j-1]
    return p

def kmp(a,s):
    m = len(a)
    n = len(s)
    p = pref_suf(a)
    i = 0
    j = 0

    while i < n:
        if s[i] == a[j]:
            i += 1
            j += 1
            if j == m: # если дошли до конца искомой строки
                return i - m
        else:
            if j > 0:
                j = p[j-1]
            else:
                i += 1

    return 'no matching'

print(kmp(a,s))