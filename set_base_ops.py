"""
集合基本操作
"""

def main() -> None:
    a = {1, 2, 3, 4, 5}
    b = {2, 4, 6, 8, 10}
    '''并、交、差、异或、子集'''
    # 并
    print(a | b)      # 方法一
    print(a.union(b)) # 方法二
    # 交
    print(a & b)             # 方法一
    print(a.intersection(b)) # 方法二
    # 差
    print(a - b)           # 方法一
    print(a.difference(b)) # 方法二
    # 异或
    print(a ^ b)                     # 方法一
    print(a.symmetric_difference(b)) # 方法二
    # 子集
    print(a <= b)        # 方法一
    print(a.issubset(b)) # 方法二
    '''添加、删除、是否空集'''
    # 向集合中添加尚不存在的元素
    a.add(6)
    print(a)
    # 向集合中添加已存在的元素，为无效操作
    a.add(5)
    print(a)
    # 判断是否为空集（方式一）
    print(len(a) == 0)
    # 判断是否为空集（方式二）
    print(a | set() == set())

if __name__ == '__main__':
    main()