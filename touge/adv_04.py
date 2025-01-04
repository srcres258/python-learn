from typing import List
import sys
from math import sqrt


class Point:
    __slots__ = 'x', 'height'

    def __init__(self, x = 0.0, height = None) -> None:
        if height is None:
            height = [0.0] * 5
        self.x: float = x
        self.height: List[float] = height


def new_2d_arr_int(d1_len: int, d2_len: int, init_val: int = 0) -> List[List[int]]:
    result = list()
    for i in range(d2_len):
        result.append([init_val] * d1_len)
    return result


def new_2d_arr_float(d1_len: int, d2_len: int, init_val: float = 0.0) -> List[List[float]]:
    result = list()
    for i in range(d2_len):
        result.append([init_val] * d1_len)
    return result


n: int; t: List[List[int]] = new_2d_arr_int(200, 200)
# The Floyd algorithm requires the initial array value to be maximum.
w: List[List[float]] = new_2d_arr_float(200, 200, sys.float_info.max)
a: List[Point] = [Point() for _ in range(200)]


if __name__ == '__main__':
    n = int(input())
    # Input wall information.
    for i in range(1, n + 1):
        line = input().split()
        x = float(line[0])
        a1 = float(line[1])
        b1 = float(line[2])
        a2 = float(line[3])
        b2 = float(line[4])
        a[i].x = x
        a[i].height[1] = a1
        a[i].height[2] = b1
        a[i].height[3] = a2
        a[i].height[4] = b2

    # For the ii-th column.
    for ii in range(2, n + 1):
        for i in range(1, 5):
            # For the jj-th column
            for jj in range(1, ii):
                for j in range(1, 5):
                    # The line equation connecting the i-th point and the j-th point is going
                    # to be calculated during this loop layer.

                    # The two coordinates of the two points of the current enumeration.
                    x1 = a[ii].x; y1 = a[ii].height[i]
                    x2 = a[jj].x; y2 = a[jj].height[j]
                    judge = True
                    # The wall between them.
                    for kk in range(jj + 1, ii):
                        x = a[kk].x
                        # The equation of corresponding coordinates of the points within this two columns,
                        # With the information from the kk-th column's points included.
                        y0 = ((y2 - y1) * (x - x1) / (x2 - x1)) + y1

                        if a[kk].height[1] <= y0 <= a[kk].height[2] or a[kk].height[3] <= y0 <= a[kk].height[4]:
                            # If the line is within the hole, accept.
                            judge = True
                        else:
                            # Otherwise, refuse and stop calculating immediately.
                            judge = False
                            break
                    if judge: # If this line is acceptable.
                        fr = (jj - 1) * 4 + j; to = (ii - 1) * 4 + i # Get the ordinals of the two points.
                        t[fr][0] += 1 # Increase the out degree of the starting point.
                        t[fr][t[fr][0]] = to
                        # Let the weight be the distance between the two points.
                        w[fr][to] = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # This is the point from the starting point to points from other walls
    # (excluding the terminal point).
    for jj in range(1, n + 1):
        for j in range(1, 5):
            # One point (the starting point) has become fixed from now on.
            x1 = 0; y1 = 5
            # Now we only need to enumerate through the other point.
            x2 = a[jj].x; y2 = a[jj].height[j]
            # If there are no walls between them, the line is absolutely acceptable,
            # hence the initial value is true.
            judge = True
            # Then enumerate through the walls between them.
            for kk in range(1, jj):
                x = a[kk].x
                # Judge whether the line is acceptable with the same approach.
                y0 = ((y2 - y1) * (x - x1) / (x2 - x1)) + y1
                if a[kk].height[1] <= y0 <= a[kk].height[2] or a[kk].height[3] <= y0 <= a[kk].height[4]:
                    judge = True
                else:
                    judge = False
                    break
            if judge:
                # If acceptable, add this line.
                fr = 0; to = (jj - 1) * 4 + j
                t[fr][0] += 1
                t[fr][t[fr][0]] = to
                w[fr][to] = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Points from the other walls to the terminal point (ordinal 4 * n + 1).
    for jj in range(1, n + 1):
        for j in range(1, 5):
            x1 = a[jj].x; y1 = a[jj].height[j]
            # And now one point becomes the terminal point.
            x2 = 10; y2 = 5
            judge = True
            for kk in range(jj + 1, n + 1):
                x = a[kk].x
                y0 = ((y2 - y1) * (x - x1) / (x2 - x1)) + y1
                if a[kk].height[1] <= y0 <= a[kk].height[2] or a[kk].height[3] <= y0 <= a[kk].height[4]:
                    judge = True
                else:
                    judge = False
                    break
            if judge:
                # If acceptable, add this line.
                fr = (jj - 1) * 4 + j; to = 4 * n + 1
                t[fr][0] += 1
                t[fr][t[fr][0]] = to
                w[fr][to] = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Finally calculate between the starting point and the terminal one.
    # Because there is a situation that line connecting the start and the end is acceptable as well,
    # this judgement is required. Otherwise we may obtain an WRONG answer!

    # The two points are fixed now.
    x1 = 0; y1 = 5
    x2 = 10; y2 = 5
    judge = True
    for kk in range(1, n + 1):
        x = a[kk].x
        y0 = ((y2 - y1) * (x - x1) / (x2 - x1)) + y1
        if a[kk].height[1] <= y0 <= a[kk].height[2] or a[kk].height[3] <= y0 <= a[kk].height[4]:
            judge = True
        else:
            judge = False
            break
    if judge:
        # If not intercepted, the line must be accepted.
        fr = 0; to = 4 * n + 1
        t[fr][0] += 1
        t[fr][t[fr][0]] = to
        w[fr][to] = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Let n be the point ordinal.
    n = 4 * n + 1
    # Carry out the Floyd algorithm from 0 to n.
    for k in range(0, n + 1):
        for i in range(0, n + 1):
            for j in range(0, n + 1):
                if w[i][j] > w[i][k] + w[k][j]:
                    w[i][j] = w[i][k] + w[k][j]
    # Output the result according to the given format.
    print("%.2lf" % w[0][n])
