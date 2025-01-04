if __name__ == '__main__':
    max_ = 1
    min_ = 1000
    count = [0] * 26
    str_ = input().strip()
    for i in range(len(str_)):
        count[ord(str_[i]) - 97] += 1
    for j in range(26):
        if count[j] > max_:
            max_ = count[j]
        if count[j] != 0 and count[j] < min_:
            min_ = count[j]
    print(max_ - min_)
