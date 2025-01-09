if __name__ == '__main__':
    s = input()
    cnt = len(s)
    MAX = 5005
    s_ = [chr(0)] * MAX
    dp = [[chr(0)] * MAX for _ in range(2)]
    for i in range(cnt):
        s_[cnt - i - 1] = s[i]
    for i in range(1, cnt + 1):
        for j in range(1, cnt + 1):
            x = i - 1
            y = j - 1
            l = (i % 2) ^ 1
            if s[x] == s_[y]:
                dp[i % 2][j] = chr(ord(dp[(i % 2) ^ 1][j - 1]) + 1)
            else:
                dp[i % 2][j] = chr(max(ord(dp[(i % 2) ^ 1][j]), ord(dp[i % 2][j - 1])))
    print(cnt - ord(dp[cnt % 2][cnt]))
