# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-5-28
UpdateTime: 2019-12-5
Info: 哈希查找

算法简介--哈希查找

   哈希表就是一种以键-值(key-indexed) 存储数据的结构，只要输入待查找的值即key，即可查找到其对应的值。
算法思想
    哈希的思路很简单，如果所有的键都是整数，那么就可以使用一个简单的无序数组来实现：
    将键作为索引，值即为其对应的值，这样就可以快速访问任意键的值。
    这是对于简单的键的情况，我们将其扩展到可以处理更加复杂的类型的键。
算法流程
　　1）用给定的哈希函数构造哈希表；
　　2）根据选择的冲突处理方法解决地址冲突；常见的解决冲突的方法：拉链法和线性探测法。
　　3）在哈希表的基础上执行哈希查找。
复杂度分析
　　单纯论查找复杂度：对于无冲突的Hash表而言，查找复杂度为O(1)（注意，在查找之前我们需要构建相应的Hash表）。
"""
# 单纯论查找复杂度：对于无冲突的Hash表而言，查找复杂度为O(1)（注意，在查找之前我们需要构建相应的Hash表）。

# 除法取余法实现的哈希函数
def myHash(data, hashLength):
    return data % hashLength

# 哈希表检索数据
def searchHash(hash, hashLength, data):
    hashAddress = myHash(data, hashLength)
    while hash.get(hashAddress) and hash[hashAddress] != data:#指定hashAddress存在，但并非关键值，则用开放寻址法解决
        hashAddress += 1
        hashAddress = hashAddress % hashLength
    if hash.get(hashAddress) == None:
        return False
    return True

# 数据插入哈希表
def insertHash(hash, hashLength, data):
    hashAddress = myHash(data, hashLength)
    while(hash.get(hashAddress)):#如果key存在说明应经被别人占用,需要解决冲突
        hashAddress += 1 #用开放寻执法
        hashAddress = myHash(hashAddress, hashLength)
    hash[hashAddress] = data

if __name__ == '__main__':
    list = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    hashLength = len(list) + 1
    hash = {}
    print("length:%s list:%s"%(hashLength,list))
    for i in list:
        insertHash(hash, hashLength, i)
    result = searchHash(hash, hashLength, 3)
    print("List key is:", result)