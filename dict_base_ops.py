"""
字典基本操作
"""

def main() -> None:
    mydict = { 1: 'Mon', 'line1': 3332 }
    '''添加、删除、是否空字典'''
    # 向字典中添加键值对
    mydict[2] = '2'
    print(mydict)
    # 从字典中删除键值对
    del mydict[1]
    print(mydict)
    # 判断字典是否为空
    print(len(mydict) == 0)
    '''取字典中所有的key/value'''
    # 取字典中所有的键（key）
    print(list(mydict.keys()))
    # 取字典中所有的值（value）
    print(list(mydict.values()))
    '''判断key是否存在'''
    print('line1' in mydict.keys()) # 方式一
    print('line1' in mydict)        # 方式二

if __name__ == '__main__':
    main()