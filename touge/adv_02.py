def main():
    avail = [True] * 30 # Whether the person is within the queue or not.
    out_record = [] # Indexes of people passed.
    base = int(input()) # Which index of person is going to be passed.

    cur = 0
    num = 0
    while len(out_record) < 15: # 15 people are going to be passed.
        if avail[cur]:
            if num % base == base - 1:
                out_record.append(cur)
                avail[cur] = False
            num += 1
        cur += 1
        if cur == len(avail):
            cur = 0

    for i in range(len(out_record)):
        out_record[i] += 1
    print(out_record)


if __name__ == '__main__':
    main()
