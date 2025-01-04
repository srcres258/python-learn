from typing import List
import sys


N: int = 20
dx: List[int] = [0, 0, 1, -1]; dy: List[int] = [1, -1, 0, 0]
sum: int = 0
ans: int = sys.maxsize
n: int; m: int
val: List[List[int]] = [[0] * N for _ in range(N)]
st: List[List[bool]] = [[False] * N for _ in range(N)]


def dfs(x: int, y: int, cnt: int, v: int) -> None:
    global ans

    if v == sum // 2:
        ans = min(ans, cnt)
        return
    if v > sum // 2:
        return
    for i in range(4):
        a = x + dx[i]; b = y + dy[i]
        if a < 1 or b < 1 or a > m or b > n:
            continue
        if st[a][b]:
            continue
        st[a][b] = True
        dfs(a, b, cnt + 1, v + val[a][b])
        st[a][b] = False


if __name__ == '__main__':
    data = input().strip().split()
    n = int(data[0])
    m = int(data[1])
    for i in range(1, n + 1):
        data = input().strip().split()
        for j in range(1, m + 1):
            val[i][j] = int(data[j - 1])
            sum += val[i][j]
    if sum % 2 == 0:
        st[1][1] = True
        dfs(1, 1, 1, val[1][1])
    print(0 if ans == sys.maxsize else ans)
