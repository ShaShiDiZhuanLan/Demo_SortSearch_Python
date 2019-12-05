# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-5-28
UpdateTime: 2019-12-5
Info: 分块查找

算法简介--分块查找

      要求是顺序表，分块查找又称索引顺序查找，它是顺序查找的一种改进方法。
算法思想
    将n个数据元素"按块有序"划分为m块（m ≤ n）。
    每一块中的结点不必有序，但块与块之间必须"按块有序"；
    即第1块中任一元素的关键字都必须小于第2块中任一元素的关键字；
    而第2块中任一元素又都必须小于第3块中的任一元素，……
算法流程　
    1、先选取各块中的最大关键字构成一个索引表；
    2、查找分两个部分：先对索引表进行二分查找或顺序查找，以确定待查记录在哪一块中；
    3、在已确定的块中用顺序法进行查找。
复杂度分析
    时间复杂度：O(log(m)+N/m)
"""
# 时间复杂度：O(log(m)+N/m)
# 1、先选取各块中的最大关键字构成一个索引表
# 2、查找分两个部分：先对索引表进行二分查找或顺序查找，以确定待查记录在哪一块中
# 3、在已确定的块中用顺序法进行查找

# 二分查找
def binary_search(list, key):
    length = len(list)
    first = 0
    last = length - 1
    # print("length:%s list:%s"%(length,list))
    while first <= last:
        mid = (last + first) // 2
        if list[mid] > key:
            last = mid - 1
        elif list[mid] < key:
            first = mid + 1
        else:
            # return mid
            return True
    return False

# 分块查找
def block_search(list, count, key):
    length = len(list)
    block_length = length//count
    if count * block_length != length:
        block_length += 1
    # print("block_length:", block_length) # 块的多少
    for block_i in range(block_length):
        block_list = []
        for i in range(count):
            if block_i*count + i >= length:
                break
            block_list.append(list[block_i*count + i])
        result = binary_search(block_list, key)
        if result != False:
            # return block_i*count + result
            return True
    return False

if __name__ == '__main__':
    list = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = block_search(list, 4, 444) # 第二个参数是块的长度，最后一个参数是要查找的元素
    print("List key is:", result)