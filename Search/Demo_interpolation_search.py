# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-5-28
UpdateTime: 2019-12-5
Info: 插值查找

算法简介--插值查找

    插值查找是根据要查找的关键字key与查找表中最大最小记录的关键字比较后的 查找方法，其核心就在于插值的计算公式 (key-a[low])/(a[high]-a[low])*(high-low)。
    时间复杂度o(logn)但对于表长较大而关键字分布比较均匀的查找表来说，效率较高。
算法思想
    基于二分查找算法，将查找点的选择改进为自适应选择，可以提高查找效率。当然，差值查找也属于有序查找。
    注：对于表长较大，而关键字分布又比较均匀的查找表来说，插值查找算法的平均性能比折半查找要好的多。反之，数组中如果分布非常不均匀，那么插值查找未必是很合适的选择。
复杂度分析
    时间复杂性：如果元素均匀分布，则O（log log n）），在最坏的情况下可能需要 O（n）。
    空间复杂度：O（1）。
"""
# 时间复杂性：如果元素均匀分布，则O（log log n）），在最坏的情况下可能需要 O（n）。
# 空间复杂度：O（1）。

# 插值查找算法
def interpolation_search(list, key):
    length = len(list)
    low = 0
    high = length - 1
    time = 0
    # print("length:%s list:%s"%(length,list))
    while low < high:
        time += 1
        mid = low + int((high - low) * (key - list[low]) / (list[high] - list[low]))# 计算mid值是插值算法的核心代码
        if key < list[mid]:
            high = mid - 1
        elif key > list[mid]:
            low = mid + 1
        else:
            # return mid
            return True
    return False

if __name__ == '__main__':
    list = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = interpolation_search(list, 7)
    print("List key is:", result)