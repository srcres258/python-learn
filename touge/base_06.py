from typing import List


N: int = 1005
arr: List[List[int]] = [[0] * N for _ in range(N)]


if __name__ == '__main__':
    data = input().strip().split()
    n = int(data[0])
    m = int(data[1])
    for i in range(n):
        data = input().strip().split()
        for j in range(m):
            arr[i][j] = int(data[j])
    for i in range(m):
        for j in range(n):
            print(arr[j][m - 1 - i], end=" " if j < n - 1 else "")
        print()
