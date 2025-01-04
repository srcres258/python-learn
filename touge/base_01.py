if __name__ == '__main__':
    n = int(input().strip())
    data = input().strip().split()
    a = [0] * 1000
    for i in range(n):
        a[i] = int(data[i])
    max_ = 0
    for i in range(n - 1):
        if max_ < abs(a[i + 1] - a[i]):
            max_ = abs(a[i + 1] - a[i])
    print(max_)
