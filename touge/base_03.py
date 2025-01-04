if __name__ == '__main__':
    j = 0
    n = int(input().strip())
    data = input().strip().split()
    t = 0
    for i in range(1, n + 1):
        x = int(data[i - 1])
        if x != t:
            j += 1
        t = x
    print(j)
