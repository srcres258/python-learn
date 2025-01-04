from typing import List


N: int = 1000007
la: int
lb: int
next_: List[int] = [0] * N
a: List[int] = [0] * N
b: List[int] = [0] * N


def next() -> None:
    j = 0
    for i in range(2, lb + 1):
        while j > 0 and b[i] != b[j + 1]:
            j = next_[j]
        if b[i] == b[j + 1]:
            j += 1
        next_[i] = j


def kmp(a: List[int], b: List[int]) -> int:
    j = 0
    t = 0
    l = -1
    for i in range(1, la + 1):
        while j > 0 and b[j + 1] != a[i]:
            j = next_[j]
        if b[j + 1] == a[i]:
            j += 1
        if j == lb:
            t = i - lb + 1
            l = 0
            break
    if l == 0:
        while t <= la:
            print(chr(a[t]), end='')
            t += 1
    return l


def main() -> None:
    global la, lb

    s = input().strip()
    for i, c in enumerate(s):
        a[i + 1] = ord(c)
    la = len(s)
    n = int(input().strip())
    for i in range(n):
        s = input().strip()
        for j, c in enumerate(s):
            b[j + 1] = ord(c)
        lb = len(s)
        next()
        m = kmp(a, b)
        if m == -1:
            print("Not Found", end='')
        if i != n - 1:
            print()


if __name__ == '__main__':
    main()
