from typing import List


MAXN: int = int(5e5 + 10)
n: int
a: List[int] = [0] * MAXN
deg: List[int] = [0] * MAXN
vis: List[bool] = [False] * MAXN
ans: int = 0


def dfs(x: int, col: int) -> None:
    global ans

    if vis[x]:
        return
    vis[x] = True
    ans += col
    deg[a[x]] -= 1
    if not deg[a[x]] or col == 1:
        dfs(a[x], col ^ 1)


def main():
    global n

    n = int(input().strip())
    for i in range(1, n + 1):
        a[i] = int(input().strip())
        deg[a[i]] += 1
    for i in range(1, n + 1):
        if not deg[i]:
            dfs(i, 1)
    for i in range(1, n + 1):
        if not vis[i]:
            dfs(i, 0)
    print(ans)


if __name__ == '__main__':
    main()
