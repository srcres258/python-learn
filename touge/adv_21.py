if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    a = [[' '] * 1005 for _ in range(1005)]
    for i in range(n):
        data = input()
        for j in range(m):
            a[i][j] = data[j]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'h':
                if a[i + 1][j] == 'e' and a[i + 2][j] == 'h' and a[i + 3][j] == 'e':
                    cnt += 1
                if a[i][j + 1] == 'e' and a[i][j + 2] == 'h' and a[i][j + 3] == 'e':
                    cnt += 1
            if a[i][j] == 'e':
                if a[i + 1][j] == 'h' and a[i + 2][j] == 'e' and a[i + 3][j] == 'h':
                    cnt += 1
                if a[i][j + 1] == 'h' and a[i][j + 2] == 'e' and a[i][j + 3] == 'h':
                    cnt += 1
    print(cnt)
