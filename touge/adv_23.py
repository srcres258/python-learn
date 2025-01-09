from queue import Queue


if __name__ == '__main__':
    m, n = map(int, input().strip().split())
    words = [int(x) for x in input().strip().split()]
    s = set()
    q = Queue()
    sum_ = 0
    for i in range(n):
        word = words[i]
        if word not in s:
            if q.qsize() < m:
                q.put_nowait(word)
            else:
                it = q.get_nowait()
                s.remove(it)
                q.put_nowait(word)
            s.add(word)
            sum_ += 1
    print(sum_)
