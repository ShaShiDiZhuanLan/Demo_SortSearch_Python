# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-5-28
UpdateTime: 2019-12-5
Info: 桶排序

桶排序是计数排序的升级版。

它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要做到这两点：
1、在额外空间充足的情况下，尽量增大桶的数量
2、使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中
同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。

最快：当输入的数据可以均匀的分配到每一个桶中。
最慢：当输入的数据被分配到了同一个桶中。
"""

# 桶排序
def bucketSort(arr):
    # 选择一个最大的数
    max_num = max(arr)
    # 创建一个元素全是0的列表, 当做桶
    bucket = [0] * (max_num + 1)
    # 把所有元素放入桶中, 即把对应元素个数加一
    for i in arr:
        bucket[i] += 1
    # 存储排序好的元素
    sort_nums = []
    # 取出桶中的元素
    for j in range(len(bucket)):
        if bucket[j] != 0:
            for y in range(bucket[j]):
                sort_nums.append(j)
    return sort_nums

if __name__ == '__main__':
    list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    print("List source is:", list)
    result = bucketSort(list)
    print("List sort is:", result)