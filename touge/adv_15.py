from math import sqrt


if __name__ == '__main__':
    aa = [0] * 200001
    bb = [0] * 200001

    n = int(input().strip())
    cnt = 0
    m = 0
    data = [int(x) for x in input().strip().split()]
    for i in range(n):
        aa[i] = data[i]

        h = aa[i]

        while h > 1:
            bb[i] += 1
            h = int(sqrt(h // 2 + 1))
        m = max(m, bb[i])

    for k in range(m, 0, -1):
        for i in range(n):
            if bb[i] == k:
                bb[i] -= 1

                if aa[i] != aa[i + 1]:
                    cnt += 1

                aa[i] = int(sqrt(aa[i] // 2 + 1))

    print(cnt)
