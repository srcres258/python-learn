if __name__ == '__main__':
    N = int(input().strip())
    count = [int(x) for x in input().strip().split()]

    zw = [[0] * 6 for _ in range(20)]
    for i in range(len(zw)):
        zw[i][5] = 5

    for i in range(N):
        temp = count[i]
        flag = False
        for j in range(len(zw)):
            res = zw[j][5]
            if res >= temp:
                start = 5 - res
                zw[j][5] -= count[i]
                flag = True
                for k in range(start, start + count[i]):
                    print(j * 5 + k + 1, end=' ' if k < start + count[i] - 1 else '\n')
                break
        if not flag:
            for j in range(len(zw)):
                res = zw[j][5]
                if res > 0:
                    print(j * 5 + 5 - res + 1)
                    zw[j][5 - res] = 1
                    zw[j][5] -= temp
                    temp -= 1
                if temp == 0:
                    break
                else:
                    print(' ')
            print()
