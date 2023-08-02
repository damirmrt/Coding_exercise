'''
Write a code to calculate the number of points laying inside of a sphere with radius R.
Input is (N, D) array where N is a number of points, and D is dimensionality.

print(points_in_sphere(np.array(
[[0.5, 0.5, 0.5],
 [0.5, 0.5, 1.5],
 [0.5, 1.5, 1.5],
 [0.5, 0.15, 0.15]]), 1.0))


'''

def solution (points, r):
    counter = 0
    for i in range(len(points)):
        tmp = 0
        for j in points[i]:
            tmp += j**2
        if tmp <= r**2:
            counter += 1
    return counter

points = [[0.5, 0.5, 0.5], [0.5, 0.5, 0.8], [0.5, 1.5, 1.5], [0.5, 0.15, 0.15]]

print(solution(points,2))