from math import sqrt


def get_num(first: float, second: float) -> int:
    count = 0
    for i in range(int(first), int(second) + 1):
        count += 1
    if first - int(first) > 0:
        count -= 1
    return count


def main():
    N, L, R = map(int, input().strip().split())
    first = sqrt(L)
    second = sqrt(R)
    result = get_num(first, second)
    result = int(R - L + 1 - result)
    print(result - (result >> 32 << 32))


if __name__ == '__main__':
    main()
