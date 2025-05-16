'''
name1 = str(input())
name2 = str(input())

print(
    f'{name1} and {name2} sat in the tree. \n{name1} had fallen,'
    f' {name2} was stolen.\nWhat\'s remaining in the tree?')

'''
'''
n = int(input())
t = ''
for i in range(n+1):
    t+=(str(i)+' ')*i

print(t[:n*2-1])
'''

'''
def f(x):
    if x <= -2:
        1 - (x + 2) ** 2
    elif x > -2 and x <= 2:
        -x / 2
    else:
        (x - 2) ** 2 + 1
    return x

print(f(20))

'''
'''
from math import exp
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-15,15,0.1)


def func(x):
    return (1/(1+exp(-x))) * (1 - (1/(1+exp(-x))))


y = [func(i) for i in x]
plt.plot(x, y)
plt.show()
print(max(y))

'''
'''
a = ''
while a != "End":
    a = str(input())
    if a != "End":
        print(f'Processing "{a}" command...')
    else:
        print('Good bye!')
        
'''
'''
counter = 1
s = 'aaabccccCCaB'
s += ' '
r = ""
for i in range(1,len(s)):
    if s[i] != s[i-1] and counter < 2:
        r += s[i-1]
    elif s[i] != s[i-1] and counter >= 2:
        r += str(counter)
        r += s[i-1]
        counter = 1
    else:
        counter += 1

print(r)
'''

'''
s = "15.5 mile in km"
l = s.split(sep= ' ')
info = {'mile': 1609,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254,
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001}

ans = float(l[0])*info[l[1]]/info[l[3]]
print('{:3.2e}'.format(ans))
'''

ransomNote = "aa"
magazine = "baabbb"

dm = {}
for m in magazine:
    dm[m] = 1 + dm.get(m, 0)

for n in ransomNote:
    if n in dm and dm[n] > 0:
        dm[n] -= 1
    else:
        print(False)

print(True)