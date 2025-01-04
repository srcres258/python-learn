if __name__ == '__main__':
    n = int(input().strip())
    count = 0
    a = [0] * 100000
    while n != 0:
        n -= 1
        a[count] = n % 26
        count += 1
        n //= 26
    for i in range(count - 1, -1, -1):
        print(chr(a[i] + ord('A')), end='')
    print()
