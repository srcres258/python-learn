from queue import Queue
from typing import List


n: int; m: int; x: int; y: int
q: Queue = Queue(); q1: Queue = Queue()
a: List[List[int]] = [[0] * 410 for _ in range(410)]
b: List[List[int]] = [[-1] * 410 for _ in range(410)]
dx: List[int] = [-2, -2, 2, 2, 1, -1, 1, -1]
dy: List[int] = [-1, 1, -1, 1, 2, -2, -2, 2]


def bfs() -> None:
    while not q.empty():
        for i in range(8):
            xx = q.queue[0] + dx[i]
            yy = q1.queue[0] + dy[i]
            if 0 < xx <= n and 0 < yy <= m and not a[xx][yy]:
                a[xx][yy] = 1
                b[xx][yy] = b[q.queue[0]][q1.queue[0]] + 1
                q.put_nowait(xx)
                q1.put_nowait(yy)
        q.get_nowait()
        q1.get_nowait()


def main() -> None:
    global n, m, x, y

    n, m, x, y = tuple([int(x) for x in input().strip().split()])
    q.put_nowait(x)
    q1.put_nowait(y)
    a[x][y] = 1
    b[x][y] = 0
    bfs()
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(("%-5d" if j < m else "%d") % b[i][j], end="")
        print()


if __name__ == '__main__':
    main()
