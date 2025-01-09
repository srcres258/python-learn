if __name__ == '__main__':
    m, n = map(int, input().strip().split())
    a = list()
    for _ in range(m):
        a.append([int(x) for x in input().strip().split()])
    x, y, s, k = tuple(input().strip().split())
    x = int(x)
    y = int(y)
    k = int(k)
    while k:
        if a[x][y] == 1:
            a[x][y] = 0
            if s == 'U':
                s = 'R'
                y += 1
            elif s == 'R':
                s = 'D'
                x += 1
            elif s == 'D':
                s = 'L'
                y -= 1
            else:
                s = 'U'
                x -= 1
        else:
            a[x][y] = 1
            if s == 'U':
                s = 'L'
                y -= 1
            elif s == 'L':
                s = 'D'
                x += 1
            elif s == 'D':
                s = 'R'
                y += 1
            else:
                s = 'U'
                x -= 1
        k -= 1
    print(x, y)
