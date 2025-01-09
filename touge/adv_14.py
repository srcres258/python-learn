if __name__ == '__main__':
    n = int(input().strip())
    s = [0] * 3010
    for i in range(1, n + 1):
        s[i] = ord(input().strip())
    a = 1
    b = n
    i = 1
    while i <= n:
        j = i
        while j <= i + 79 and j <= n:
            if s[a] == s[b]:
                p = a
                q = b
                while s[p] == s[q]:
                    p += 1
                    q -= 1
                if s[p] <= s[q]:
                    print(chr(s[a]), end='')
                    a += 1
                else:
                    print(chr(s[b]), end='')
                    b -= 1
            else:
                if s[a] > s[b]:
                    print(chr(s[b]), end='')
                    b -= 1
                else:
                    print(chr(s[a]), end='')
                    a += 1
            j += 1
        i += 80
    print()
