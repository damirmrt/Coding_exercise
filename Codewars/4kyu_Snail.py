'''
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

Main idea in my solution is using four pointer. One pointer for each side of 2D array.
On first cycle you iterate ove outer edge of array,
then increment/decrement all pointers by 1 and repeat till you reach center
'''
def snail(snail_map):
    if len(snail_map) == 1:
        return snail_map[0]
    else:
        res = []

        l = 0
        r = len(snail_map)
        t = 0
        b = len(snail_map)

        while l < r:
            for i in range(l,r):
                res.append(snail_map[t][i])

            for i in range(t+1,b-1):
                res.append(snail_map[i][r-1])

            for i in range(r-1,l-1, -1):
                if t < b-1:
                    res.append(snail_map[b-1][i])

            for i in range(b-2,t , -1):
                res.append(snail_map[i][l])

            l += 1
            r -= 1
            b -= 1
            t += 1

        return res

