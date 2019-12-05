# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-5-28
UpdateTime: 2019-12-5
Info: 二叉树查找（BST）

算法简介--二叉树查找（BST）

    二叉查找树是先对待查找的数据进行生成树，确保树的左分支的值小于右分支的值，然后在就行和每个节点的父节点比较大小，查找最适合的范围。
    这个算法的查找效率很高，但是如果使用这种查找方法要首先创建树。
算法思想
　　二叉查找树（BinarySearch Tree）或者是一棵空树，或者是具有下列性质的二叉树：
　　    1）若任意节点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
　　    2）若任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
　　    3）任意节点的左、右子树也分别为二叉查找树。
　　二叉查找树性质：对二叉查找树进行中序遍历，即可得到有序的数列。

     复杂度分析
     它和二分查找一样，插入和查找的时间复杂度均为O(logn)，但是在最坏的情况下仍然会有O(n)的时间复杂度。
     原因在于插入和删除元素的时候，树没有保持平衡。
"""
# ----- 二叉树查找（BST） -----
# 1、广度优先BFS--查找
# 2、前序遍历--查找
# 3、中序遍历--查找
# 4、后序遍历--查找

class Node(object):
    def __init__(self, element, lchild=None, rchild=None):
        self.element = element
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    def __init__(self, root=None):
        self.list = []
        self.root = root
        self.preorder_find = False
        self.inorder_find = False
        self.postorder_find = False
    # 增加树节点
    def add(self, item):
        self.list.append(item)
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur_node = queue.pop()
                if cur_node.lchild is None:
                    cur_node.lchild = node
                    return
                elif cur_node.rchild is None:
                    cur_node.rchild = node
                    return
                else:
                    queue.append(cur_node.lchild)
                    queue.append(cur_node.rchild)
    # 广度优先BFS
    def width_circle(self, key):
        if self.root is None:
            return ' '
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur_node = queue.pop()
                # print(cur_node.element, end=' ')
                if cur_node.element == key:
                    return True
                if cur_node.rchild is not None:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is not None:
                    queue.append(cur_node.rchild)
        return False
    # 前序遍历
    def preorder(self, node, key):
        if node == None:
            return
        print(node.element, end=' ')
        self.preorder(node.lchild, key)
        self.preorder(node.rchild, key)
        if node.element == key:
            print("\n_______________________find it:%s_______________________"%key)
            self.preorder_find = True
    # 中序遍历
    def inorder(self, node, key):
        if node == None:
            return
        self.inorder(node.lchild, key)
        print(node.element, end=' ')
        if node.element == key:
            print("\n_______________________find it:%s_______________________"%key)
            self.inorder_find = True
        self.inorder(node.rchild, key)
    # 后序遍历
    def postorder(self, node, key):
        if node == None:
            return
        self.postorder(node.lchild, key)
        self.postorder(node.rchild, key)
        print(node.element, end=' ')
        if node.element == key:
            print("\n_______________________find it:%s_______________________"%key)
            self.postorder_find = True

if __name__ == '__main__':
    t = Tree()
    list = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    key = 12
    for item in list:
        t.add(item)
    print("Length: %s\nList: %s"%(len(list),list))

    print("\n广度优先BFS:")
    result = t.width_circle(key)
    print("\nList key is:", result)

    print("\n前序遍历:")
    t.preorder(t.root, key)
    print("\nList key is:", t.preorder_find)

    print("\n中序遍历")
    t.inorder(t.root, key)
    print("\nList key is:", t.inorder_find)

    print("\n后序遍历")
    t.postorder(t.root, key)
    print("\nList key is:", t.postorder_find)
