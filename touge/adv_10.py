from typing import List


class Edge:
    __slots__ = 'to', 'next'

    def __init__(self, to = 0, next_ = 0):
        self.to: int = to
        self.next: int = next_


n: int
head: List[int] = [0] * 50005
cnt: int = 0
dp: List[int] = [0] * 50005
dep: List[int] = [0] * 50005
son: List[int] = [0] * 50005
e: List[Edge] = [Edge() for _ in range(100005)]


def add(u: int, v: int) -> None:
    global cnt

    cnt += 1
    e[cnt].to = v
    e[cnt].next = head[u]
    head[u] = cnt


def dfs(now: int, pre: int) -> None:
    i = head[now]
    while i != 0:
        if e[i].to != pre:
            dp[e[i].to] = dp[now] - 2 * (son[e[i].to] + 1) + n
            dfs(e[i].to, now)
        i = e[i].next


def get(now: int, pre: int) -> int:
    dep[now] = dep[pre] + 1
    num = 0
    i = head[now]
    while i != 0:
        if e[i].to != pre:
            num += 1 + get(e[i].to, now)
        i = e[i].next
    son[now] = num
    return num


def main():
    global n

    n = int(input().strip())
    for i in range(1, n):
        data = input().strip().split()
        u = int(data[0])
        v = int(data[1])
        add(u, v)
        add(v, u)
    get(1, 0)
    for i in range(1, n + 1):
        dp[1] += dep[i] - 1
    dfs(1, 0)
    id_ = 1
    min_ = dp[1]
    for i in range(2, n + 1):
        if min_ > dp[i]:
            min_ = dp[i]
            id_ = i
    print("%d %d" % (id_, dp[id_]))


if __name__ == '__main__':
    main()
