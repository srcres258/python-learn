"""
列表、元组基本操作
"""

def main() -> None:
    # + 操作
    # 作用：将两个列表合并为一个列表。
    print('+ operation')
    a = [1, 2]
    b = [3, 4, 5]
    print('a:', a)
    print('b:', b)
    print('a + b:', a + b)

    # * 操作
    # 作用：将某个列表重复给定次数以得到新列表。
    print('* operation')
    a = [1, 2]
    print('a:', a)
    print('a * 5:', a * 5)

    # len() 操作
    # 作用：获取某个列表的长度。
    print('len() operation')
    a = [1, 2, 3, 4, 5]
    print('a:', a)
    print('len(a):', len(a))

    # len() 操作
    # 作用：取列表中给定索引处的元素。
    print('[] operation')
    a = [1, 2, 3, 4, 5]
    print('a:', a)
    print('a[2]:', a[2])

    # in 操作
    # 作用：判断某元素是否位于列表中。
    print('in operation')
    a = [1, 2, 3, 4, 5]
    print('a:', a)
    print('3 in a:', 3 in a)

if __name__ == '__main__':
    main()