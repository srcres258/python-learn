from math import log, ceil


if __name__ == '__main__':
    while True:
        n = int(input().strip())
        if n == 0:
            break
        print(int(ceil(log(n) / log(3))))
