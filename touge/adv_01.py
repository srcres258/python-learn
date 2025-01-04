def transform(line: str) -> str:
    assert len(line) > 0

    result_str = ""
    cur_ch = line[0]
    cur_len = 1
    for ch in line[1:]:
        if ch == cur_ch:
            cur_len += 1
        else:
            # Char changed, record the current and begin calculating the next character.
            result_str += str(cur_len)
            result_str += cur_ch
            cur_ch = ch
            cur_len = 1
    # Record the last character.
    result_str += str(cur_len)
    result_str += cur_ch
    return result_str

def main():
    in_str = input()
    in_count = int(input())
    for _ in range(in_count):
        in_str = transform(in_str)
    print(in_str)

if __name__ == '__main__':
    main()
