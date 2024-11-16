"""
列表、元组高级操作
"""

def main() -> None:
    mylist = [1, 2, 3, 4, 5]
    '''切片：获得[2,3,4]，获得[3,4,5]，获得[3,2,1]，获得[1,3,5]'''
    # 获得[2,3,4]
    print(mylist[1:4])
    # 获得[3,4,5]
    print(mylist[2:])
    # 获得[3,2,1]
    print(mylist[2::-1])              # 方法一
    print(list(reversed(mylist[:3]))) # 方法二
    # 获得[1,3,5]
    print(mylist[0::2])

    mytpl = (1, 2, 3, 4, 5)
    '''切片：获得(2,3,4)，获得(3,4,5)，获得(3,2,1)，获得(1,3,5)'''
    # 获得[2,3,4]
    print(mytpl[1:4])
    # 获得[3,4,5]
    print(mytpl[2:])
    # 获得[3,2,1]
    print(mytpl[2::-1])               # 方法一
    print(tuple(reversed(mytpl[:3]))) # 方法二
    # 获得[1,3,5]
    print(mytpl[0::2])

    t = 'Mike and Tom'
    """split拆分、join合成为'Mike/and/Tom'"""
    print('/'.join(t.split(' ')))

if __name__ == '__main__':
    main()