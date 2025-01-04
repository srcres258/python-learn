if __name__ == '__main__':
    n = int(input().strip())
    num = [0] * 1010
    data = [int(x) for x in input().strip().split()]
    data.sort()
    for i in range(n):
        num[i] = data[i]

    mid = n // 2
    left = mid
    right = n - mid - 1

    for i in range(mid - 1, -1, -1):
        if num[i] == num[mid]:
            left -= 1
        else:
            break

    for i in range(mid + 1, n):
        if num[i] == num[mid]:
            right -= 1
        else:
            break

    if left == right:
        print(num[mid])
    else:
        print(-1)
