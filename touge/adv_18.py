if __name__ == '__main__':
    num, X, truth = tuple(input().strip().split())
    num = int(num)
    truth = int(truth)
    flag = 0
    if num == 2:
        for i in ['A', 'B', 'C', 'D', 'E']:
            j = i
            while ord(j) <= ord('E'):
                a = ((i == 'A' or j == 'A') and (i != X and j != X)) or ((i != 'A' and j != 'A') and (i == X or j == X))
                b = ((i == 'C' or j == 'C') or (i == 'E' or j == 'E'))
                c = ((i == 'C' or j == 'C') or (i == 'D' or j == 'D') or (i == 'A' or j == 'A'))
                d = ((i != 'B' and j != 'B') and (i != 'C' and j != 'C'))
                e = (i != 'E' and j != 'E')
                a = 1 if a else 0
                b = 1 if b else 0
                c = 1 if c else 0
                d = 1 if d else 0
                e = 1 if e else 0
                if a + b + c + d + e == truth:
                    if i != j:
                        flag = 1
                        print(i + j)
                j = chr(ord(j) + 1)
            if i == 'E' and flag == 0:
                print('0')
    elif num == 1:
        for i in ['A', 'B', 'C', 'D', 'E']:
            a = (i == 'A' and i != X) or (i != 'A' and i == X)
            b = (i == 'C' or i == 'E')
            c = (i == 'C' or i == 'D' or i == 'A')
            d = (i != 'B' and i != 'C')
            e = (i != 'E')
            a = 1 if a else 0
            b = 1 if b else 0
            c = 1 if c else 0
            d = 1 if d else 0
            e = 1 if e else 0
            if a + b + c + d + e == truth:
                flag = 1
                print(i)
            if i == 'E' and flag == 0:
                print('0')
