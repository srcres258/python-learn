from typing import List


N: int = int(1e5 + 10)
n: int
a: List[int] = [0] * N
num: int = 0
sum_: int = 0
flag: List[bool] = [False] * N


def dfs(be: int, ed: int) -> None:
    global num, sum_

    if flag[be]:
        if be == ed:
            num = max(num, sum_)
        return

    sum_ += 1
    flag[be] = True
    dfs(a[be], ed)
    flag[be] = False


def main() -> None:
    global n, sum_

    n = int(input().strip())
    data = input().strip().split()
    for i in range(1, n + 1):
        a[i] = int(data[i - 1])
    for i in range(1, n + 1):
        sum_ = 0
        dfs(i, i)
    print(num)


if __name__ == '__main__':
    main()
