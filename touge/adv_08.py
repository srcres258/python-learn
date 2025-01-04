from typing import List


MAX_N: int = 100005
a: List[int] = [0] * MAX_N


def main() -> None:
    n = int(input())
    lst = 0
    ans = 0
    data = input().strip().split()
    for i in range(n):
        now = int(data[i])
        if now > lst:
            ans += now - lst
        lst = now
    print(ans)


if __name__ == '__main__':
    main()
