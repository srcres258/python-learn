from typing import List


SIZE: int = 305
n: int
m: int
x: int
y: int
counts: int = 0
h: List[int] = [0] * SIZE
maxn: int = -1 << 30
id_: int = 0
get: List[bool] = [False] * SIZE


if __name__ == '__main__':
    data = input().strip().split()
    n = int(data[0])
    m = int(data[1])
    data = input().strip().split()
    for i in range(1, n + 1):
        h[i] = int(data[i - 1])
        if h[i] > maxn:
            maxn = h[i]
            id_ = i
    for i in range(m):
        data = input().strip().split()
        x = int(data[0])
        y = int(data[1])
        if h[x] > h[y]:
            if not get[y]:
                counts += 1
                get[y] = True
        elif h[x] < h[y]:
            if not get[x]:
                counts += 1
                get[x] = True
    for i in range(1, n + 1):
        if not get[i]:
            maxn = i
            break
    if counts < n - 1 or maxn != id_:
        print("no")
    else:
        print("yes")
        print(id_)
