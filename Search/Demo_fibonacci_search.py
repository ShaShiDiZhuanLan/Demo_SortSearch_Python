# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-5-28
UpdateTime: 2019-12-5
Info: 斐波那契查找

算法简介--斐波那契查找

    斐波那契数列，又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、····，
    在数学上，斐波那契被递归方法如下定义：F(1)=1，F(2)=1，F(n)=f(n-1)+F(n-2) （n>=2）。
    该数列越往后相邻的两个数的比值越趋向于黄金比例值（0.618）。
算法描述
    斐波那契查找就是在二分查找的基础上根据斐波那契数列进行分割的。
    在斐波那契数列找一个等于略大于查找表中元素个数的数F[n]，将原查找表扩展为长度为F[n](如果要补充元素，
    则补充重复最后一个元素，直到满足F[n]个元素)，完成后进行斐波那契分割，即F[n]个元素分割为前半部分F[n-1]个元素，
    后半部分F[n-2]个元素，找出要查找的元素在那一部分并递归，直到找到。
复杂度分析
    最坏情况下，时间复杂度为O(log2n)，且其期望复杂度也为O(log2n)。
"""
# 时间复杂度O(log(n))

# 斐波那契查找算法
def fibonacci_search(list, key):
    length = len(list)
    # 需要一个现成的斐波那契列表。其最大元素的值必须超过查找表中元素个数的数值。
    F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]
    low = 0
    high = length - 1
    # print("length:%s list:%s"%(length,list))

    # 为了使得查找表满足斐波那契特性，在表的最后添加几个同样的值
    # 这个值是原查找表的最后那个元素的值
    # 添加的个数由F[k]-1-high决定
    k = 0
    while high > F[k] - 1:
        k += 1
    i = high
    while F[k] - 1 > i:
        list.append(list[high])
        i += 1
    time = 0 # 算法主逻辑。time用于展示循环的次数。
    while low <= high:
        time += 1
        # 为了防止F列表下标溢出，设置if和else
        if k < 2:
            mid = low
        else:
            mid = low + F[k - 1] - 1
        if key < list[mid]:
            high = mid - 1
            k -= 1
        elif key > list[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid <= high:
                # return mid
                return True
            else:
                # return high
                return True
    return False

if __name__ == '__main__':
    list = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = fibonacci_search(list, 7)
    print("List key is:", result)