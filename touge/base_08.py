if __name__ == '__main__':
    n = int(input().strip())
    a = [int(x) for x in input().strip().split()]
    a.sort()
    if a[0] >= a[n - 1]:
        max_ = a[0]
        min_ = a[n - 1]
    else:
        max_ = a[n - 1]
        min_ = a[0]
    if n % 2 == 1:
        mid = a[n // 2]
        print("%d %d %d" % (max_, int(mid), min_))
    else:
        mid = (a[n // 2 - 1] + a[n // 2]) / 2
        if mid - int(mid) == 0:
            print("%d %d %d" % (max_, int(mid), min_))
        else:
            print("%d %.1lf %d" % (max_, mid, min_))
