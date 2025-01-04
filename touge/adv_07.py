def decrypt(pwd: str) -> str:
    while True:
        l = 0
        content = ""
        begin_idx = 0
        for i, c in enumerate(pwd):
            if c == '[':
                l += 1
                if l == 1:
                    begin_idx = i
                    continue
            if c == ']':
                l -= 1
                if l == 0:
                    break
            if l >= 1:
                content += c
        if len(content) == 0:
            break
        t = int(content[0])
        s = content[1:]
        head = pwd[:begin_idx]
        tail = pwd[begin_idx + len(content) + 2:]
        pwd = head + s * t + tail
    return pwd


if __name__ == '__main__':
    pwd = input().strip()
    print(decrypt(pwd))
