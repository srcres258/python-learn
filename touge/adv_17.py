from typing import List
from functools import cmp_to_key


class Point:
    __slots__ = 'x', 'y'

    def __init__(self, x = 0, y = 0):
        self.x: int = x
        self.y: int = y


MAXN: int = 100005
MOD: int = int(1e9 + 7)
DIF: int = 10005

points: List[Point] = [Point() for _ in range(MAXN)]
n: int
sumX: List[int] = [0] * (2 * DIF)
sumY: List[int] = [0] * (2 * DIF)
cntX: List[int] = [0] * (2 * DIF)
cntY: List[int] = [0] * (2 * DIF)
lastX: List[int] = [0] * (2 * DIF)
lastY: List[int] = [0] * (2 * DIF)
ans: int = 0


def cmp1(a: Point, b: Point) -> bool:
    if a.x != b.x:
        return a.x < b.x
    return a.y < b.y


def cmp2(a: Point, b: Point) -> bool:
    if a.x != b.x:
        return a.x < b.x
    return a.y > b.y


def cmp3(a: Point, b: Point) -> bool:
    if a.x != b.x:
        return a.x > b.x
    return a.y < b.y


def cmp4(a: Point, b: Point) -> bool:
    if a.x != b.x:
        return a.x > b.x
    return a.y > b.y


def work() -> None:
    global ans, sumX, sumY, cntX, cntY

    sumX = [0] * len(sumX)
    sumY = [0] * len(sumY)
    cntX = [0] * len(cntX)
    cntY = [0] * len(cntY)
    for i in range(n):
        x = points[i].x; y = points[i].y
        sumX[x] = (sumX[x] + int(abs(y - lastX[x])) * cntX[x]) % MOD
        cntX[x] += 1
        lastX[x] = y
        sumY[y] = (sumY[y] + int(abs(x - lastY[y])) * cntY[y]) % MOD
        cntY[y] += 1
        lastY[y] = x
        ans = (ans + sumX[x] * sumY[y]) % MOD


def main() -> None:
    global n, points

    n = int(input().strip())
    for i in range(n):
        points[i].x, points[i].y = tuple([int(x) for x in input().strip().split()])
        points[i].x += DIF
        points[i].y += DIF
    points = points[:n]
    points = sorted(points, key=cmp_to_key(lambda a, b: 1 if cmp1(a, b) else -1))
    work()
    points = sorted(points, key=cmp_to_key(lambda a, b: 1 if cmp2(a, b) else -1))
    work()
    points = sorted(points, key=cmp_to_key(lambda a, b: 1 if cmp3(a, b) else -1))
    work()
    points = sorted(points, key=cmp_to_key(lambda a, b: 1 if cmp4(a, b) else -1))
    work()
    print(ans)


if __name__ == '__main__':
    main()
