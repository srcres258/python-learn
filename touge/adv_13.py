if __name__ == '__main__':
    i = 0
    j = 0
    ci = 0
    ji = 0
    a = [0] * 10001
    b = [0] * 10001
    rains = [int(x) for x in input().strip().split()]
    for c in rains:
        if c > 0:
            a[c] -= 1
        elif c == 0:
            ci += 1
            b[j] = 999
            j += 1
        if a[c] == -1:
            b[j] = -1
            j += 1
        elif a[c] < -1:
            if ci > 0:
                ci -= 1
                for k in range(j):
                    if b[k] == 999:
                        b[k] = c
                        a[c] += 1
                        b[j] = -1
                        j += 1
                        break
        if c > i:
            i = c
    for k in range(1, i + 1):
        if a[k] < -1:
            ji = 1
            break
    if ji != 0:
        print("[]")
    else:
        for k in range(j):
            if k == 0:
                print(f"[{b[k]}, ", end='')
            elif k == j - 1:
                print(f"{b[k]}]")
            else:
                print(f"{b[k]}, ", end='')
