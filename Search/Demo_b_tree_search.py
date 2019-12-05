# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-5-28
UpdateTime: 2019-12-5
Info: B树查找

算法介绍--B树查找

一棵m阶的B树，或为空树，或为满足下列特性的m叉树：
树中每个节点至多有m棵子树
若根结点不是叶子节点，那么至少有两棵子树
除根之外的所有非终端节点至少有【m/2】（不小于m/2的最小整数）棵子树
所有叶子节点都在同一层次上

应用
如果内存和外存交换数据频繁，就会造成时间效率的瓶颈，在一个典型的B树中，如果数据量很大，无法一次性存入内存，
则可以对B树的阶数进行调整，使其与硬盘存储的页面大小相匹配，高度为h，让B树的根节点持久地保留在内存中，
那么在这棵树上寻找一个关键字至多需要读取磁盘h次。
"""

# B树查找
inorder_find = False
rinorder_find = False

#B树
class BTree:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
        self.inorder_find = False
        self.rinorder_find = False

    def insertLeft(self,value):
        self.left=BTree(value)
        return self.left

    def insertRight(self,value):
        self.right=BTree(value)
        return self.right

    def show(self):
        print(self.data)

# 插入数据
def insert(node,value):
    if value > node.data:
        if node.right:
            insert(node.right,value)
        else:
            node.insertRight(value)
    else:
        if node.left:
            insert(node.left,value)
        else:
            node.insertLeft(value)

#中序遍历：先左子树，再根节点，再右子树 从小到大排序
def inorder(node, key):
    if node.data:
        if node.left:
            inorder(node.left, key)
        node.show()
        if node.data == key:
            global inorder_find
            print("_______________________find it %s_______________________"%key)
            inorder_find = True
        if node.right:
            inorder(node.right, key)

#倒中序遍历 从大到小排序
def rinorder(node, key):  #倒中序遍历
    if node.data:
        if node.right:
            rinorder(node.right, key)
        node.show()
        if node.left:
            rinorder(node.left, key)
        if node.data == key:
            global rinorder_find
            print("_______________________find it %s_______________________"%key)
            rinorder_find = True

if __name__ == "__main__":
    list = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    key = 222
    node = BTree(list[0])
    for i in range(1,len(list)):
        insert(node,list[i])
    print("key: %s\nLength: %s\nList: %s"%(key, len(list), list))

    inorder(node,key)
    print("________________________inorder List key is:", inorder_find)

    rinorder(node,key)
    print("________________________rinorder List key is:", rinorder_find)