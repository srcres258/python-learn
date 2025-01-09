from typing import List


MAX: int = 110
e1: List[List[int]] = [list() for _ in range(MAX)]
e2: List[List[int]] = [list() for _ in range(MAX)]
match1: List[int] = [0] * MAX
match2: List[int] = [0] * MAX
vis: List[bool] = [False] * MAX
copy: List[int] = [0] * MAX
used: List[bool] = [False] * MAX
n: int; q: int; p: int
k: int; ans: int = 0


def dfs1(x: int) -> bool:
    for i in range(len(e1[x])):
        v = e1[x][i]
        if not vis[v]:
            vis[v] = True
            if match1[v] == 0 or dfs1(match1[v]):
                used[v] = True
                copy[v] = match1[v]
                match1[v] = x
                return True
    return False


def dfs2(x: int) -> bool:
    for i in range(len(e2[x])):
        v = e2[x][i]
        if vis[v]:
            continue
        vis[v] = True
        if match2[v] == 0 or dfs2(match2[v]):
            match2[v] = x
            return True
    return False


def main() -> None:
    global n, p, q, k, ans

    n, p, q = tuple([int(x) for x in input().strip().split()])
    for i in range(1, n + 1):
        data = [int(x) for x in input().strip().split()]
        for j in range(1, p + 1):
            k = data[j - 1]
            if k != 0:
                e1[i].append(j)
    for i in range(1, n + 1):
        data = [int(x) for x in input().strip().split()]
        for j in range(1, q + 1):
            k = data[j - 1]
            if k != 0:
                e2[i].append(j)
    for i in range(1, n + 1):
        for j in range(len(vis)):
            vis[j] = False
        for j in range(len(used)):
            used[j] = False
        if dfs1(i):
            for j in range(len(vis)):
                vis[j] = False
            if dfs2(i):
                ans += 1
            else:
                for j in range(1, p + 1):
                    if used[j]:
                        match1[j] = copy[j]
    print(ans)


if __name__ == '__main__':
    main()
