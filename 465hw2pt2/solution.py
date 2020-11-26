#Problem2
#Group members: Trisha Mandal, Shravan Suresh, Rohit Ghoel

import math
from collections import deque

def angle(min, point):

    if point == -1:
        return 360

    unit_right = (1, 0)
    vec = (point[0] - min[0], point[1] - min[1])
    dot = unit_right[0] * vec[0] + unit_right[1] * vec[1]
    magunit = 1
    magvec = math.sqrt((vec[0]) ** 2 + (vec[1] ** 2))
    result = math.degrees(math.acos(dot / (magunit * magvec)))
    return result

def graham_scan(points):
    minimum = min(points, key = lambda x:x[1])
    points.remove(minimum)
    points = merge_sort(points, minimum)
    points.insert(0,minimum)
    return graham_scan_core(points)

def graham_scan_core(points):
    stack = deque()

    if len(points) <=3:
        return points

    stack.append(points[0])
    stack.append(points[1])
    stack.append(points[2])

    for i in range(3,len(points)):
        p = points[i]

        while len(stack) !=0:
            pa = stack[-1]
            pb = stack[-2]
            if turnRight(pb,pa,p):
                stack.pop()

            else:
                break

        stack.append(p)
    stack = list(stack)
    stack.reverse()
    return stack


    # Merging Algorithm given in class
def turnRight(point1, point2, point3):

    vector12 = (point2[0] - point1[0], point2[1] - point1[1])
    vector23 =(point3[0] - point2[0], point3[1] - point2[1])
    if crossProduct(vector12, vector23) < 0:
        return True
    else:
        return False

def crossProduct(vector1,vector2):
    return vector1[0]*vector2[1] - vector1[1]*vector2[0]

def merge_sorted_angles(A, B, min):
    C = []
    i = 0
    j = 0
    a = len(A)
    b = len(B)
    A.append(-1)
    B.append(-1)
    for k in range(a + b):
        if angle(min, A[i]) <= angle(min, B[j]):
            C.append(A[i])
            i = i + 1
        else:
            C.append(B[j])
            j = j + 1
    return C

    # From algorithm done in class
def merge_sort(P, minimum):
    if len(P) <= 1:
        return P
    p1 = merge_sort(P[:len(P) // 2], minimum)
    p2 = merge_sort(P[len(P) // 2:], minimum)
    A = merge_sorted_angles(p1, p2, minimum)
    return A

def lowerhull(convexhull):
    smallX = min(points, key = lambda x:x[0])
    maxX = max(points, key = lambda x:x[0])

    s = convexhull.index(smallX)
    m = convexhull.index(maxX)

    if s < m:
        return convexhull[s:m+1]
    else:
        return convexhull[s:] + convexhull[:m + 1]


def upperhull(convexhull):
    smallX = min(points, key=lambda x: x[0])
    maxX = max(points, key=lambda x: x[0])

    s = convexhull.index(smallX)
    m = convexhull.index(maxX)

    if m < s:
        return convexhull[m:s + 1]

    return convexhull[m:] + convexhull[:s + 1]

points = []

n = int(input())
for i in range(n):
    temp = input().split(" ")
    tempa = float(temp[0])
    tempb = float(temp[1])
    points.append((tempa,tempb))

convexhull = graham_scan(points)
print(len(lowerhull(convexhull)), len(upperhull(convexhull)))

