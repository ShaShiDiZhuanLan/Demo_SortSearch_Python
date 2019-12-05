# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-5-28
UpdateTime: 2019-12-5
Info: 基数排序

基数排序是一种非比较型整数排序算法。

其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
"""

# 基数排序
def radix_sort(arr):
    """基数排序"""
    i = 0 # 记录当前正在排拿一位，最低位为1
    max_num = max(arr)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list =[[] for _ in range(10)] #初始化桶数组
        for x in arr:
            bucket_list[int(x / (10**i)) % 10].append(x) # 找到位置放入桶数组
        arr.clear()
        for x in bucket_list:   # 放回原序列
            for y in x:
                arr.append(y)
        i += 1
    return arr

if __name__ == '__main__':
    list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    print("List source is:", list)
    result = radix_sort(list)
    print("List sort is:", result)