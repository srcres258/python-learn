if __name__ == '__main__':
    dp = [[0] * 1000 for _ in range(1000)]
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    for i in range(1, m + 1):
        dp[i][0] = 1
        for j in range(1, n + 1):
            if i > j:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            elif i == j:
                dp[i][j] = dp[i][j - 1]
    print(dp[m][n])
