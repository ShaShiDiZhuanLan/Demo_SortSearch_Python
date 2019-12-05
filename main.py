# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-5-28
UpdateTime: 2019-12-5
Info: 所有排序查找的控制类
"""
import copy

from Sort.Demo_bubble_sort import bubbleSort # 冒泡排序
from Sort.Demo_bucket_sort import bucketSort # 桶排序
from Sort.Demo_counting_sort import countingSort # 计数排序
from Sort.Demo_heap_sort import heapSort # 堆排序
from Sort.Demo_insertion_sort import insertionSort # 插入排序
from Sort.Demo_merge_sort import mergeSort # 归并排序
from Sort.Demo_quick_sort import quickSort2 # 快速排序
from Sort.Demo_radix_sort import radix_sort # 基数排序
from Sort.Demo_selection_sort import selectionSort # 选择排序
from Sort.Demo_shell_sort import shellSort # 希尔排序

from Search import Demo_b_tree_search # B树查找
from Search import Demo_binary_search # 二分查找
from Search import Demo_binary_tree_search # 二叉树查找（BST）
from Search import Demo_block_search # 分块查找
from Search import Demo_fibonacci_search # 斐波那契查找
from Search import Demo_hash_search # 哈希查找
from Search import Demo_interpolation_search # 插值查找
from Search import Demo_sequential_search # 顺序查找

# 画线
def write_line(type):
    if type == 0:
        print("——————————————")
    else:
        print("————————————————————————————")

# 排序算法
class Demo_Sort():
    # 初始化
    def __init__(self):
        self.g_list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222] # 待排序数组

    # 冒泡排序
    def demo_bubble_sort(self):
        list = copy.copy(self.g_list)
        print("%s is source list"%list)
        result = bubbleSort(list)
        print("%s is bubble sort"%result)
        write_line(0)

    # 桶排序
    def demo_bucket_sort(self):
        list = copy.copy(self.g_list)
        print("%s is source list"%list)
        result = bucketSort(list)
        print("%s is bucket sort"%result)
        write_line(0)

    # 计数排序
    def demo_counting_sort(self):
        list = copy.copy(self.g_list)
        print("%s is source list"%list)
        result = countingSort(list,max(list))
        print("%s is counting sort"%result)
        write_line(0)

    # 堆排序
    def demo_heap_sort(self):
        list = copy.copy(self.g_list)
        print("%s is source list"%list)
        result = heapSort(list)
        print("%s is heap sort"%result)
        write_line(0)

    # 插入排序
    def demo_insertion_sort(self):
        list = copy.copy(self.g_list)
        print("%s is source list"%list)
        result = insertionSort(list)
        print("%s is insertion sort"%result)
        write_line(0)

    # 归并排序
    def demo_merge_sort(self):
        list = copy.copy(self.g_list)
        print("%s is source list"%list)
        result = mergeSort(list)
        print("%s is merge sort"%result)
        write_line(0)

    # 快速排序
    def demo_quick_sort(self):
        list = copy.copy(self.g_list)
        print("%s is source list"%list)
        result = quickSort2(list)
        print("%s is quick sort"%result)
        write_line(0)

    # 基数排序
    def demo_radix_sort(self):
        list = copy.copy(self.g_list)
        print("%s is source list"%list)
        result = radix_sort(list)
        print("%s is radix sort"%result)
        write_line(0)

    # 选择排序
    def demo_selection_sort(self):
        list = copy.copy(self.g_list)
        print("%s is source list"%list)
        result = selectionSort(list)
        print("%s is selection sort"%result)
        write_line(0)

    # 希尔排序
    def demo_shell_sort(self):
        list = copy.copy(self.g_list)
        print("%s is source list"%list)
        result = shellSort(list)
        print("%s is shell sort"%result)

    # 排序中……
    def sorting(self):
        print("Sorting...")
        write_line(1)
        self.demo_bubble_sort()
        self.demo_bucket_sort()
        self.demo_counting_sort()
        self.demo_heap_sort()
        self.demo_insertion_sort()
        self.demo_merge_sort()
        self.demo_quick_sort()
        self.demo_radix_sort()
        self.demo_selection_sort()
        self.demo_shell_sort()
        write_line(1)

# 查找算法
class Demo_Search():
    # 初始化
    def __init__(self):
        self.g_list = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
        self.g_key = 54

    # B树查找
    def demo_bTree_search(self):
        print("%s is source list, %s is key"%(self.g_list, self.g_key))
        node = Demo_b_tree_search.BTree(self.g_list[0])
        for i in range(1, len(self.g_list)):
            Demo_b_tree_search.insert(node, self.g_list[i])
        Demo_b_tree_search.inorder(node, self.g_key)
        print("bTree search: ",Demo_b_tree_search.inorder_find)
        write_line(0)

    # 二分查找
    def demo_binary_search(self):
        print("%s is source list, %s is key"%(self.g_list, self.g_key))
        result = Demo_binary_search.binary_search(self.g_list, self.g_key)
        print("binary search: ",result)
        write_line(0)

    # 二叉树查找（BST）
    def demo_binary_tree_search(self):
        print("%s is source list, %s is key"%(self.g_list, self.g_key))
        t = Demo_binary_tree_search.Tree()
        for item in self.g_list:
            t.add(item)
        result = t.width_circle(self.g_key)
        print("binary tree search: ", result)
        write_line(0)

    # 分块查找
    def demo_block_search(self):
        print("%s is source list, %s is key"%(self.g_list, self.g_key))
        result = Demo_block_search.block_search(self.g_list, 4, self.g_key) # 第二个参数是块的长度，最后一个参数是要查找的元素
        print("block search: ",result)
        write_line(0)

    # 斐波那契查找
    def demo_fibonacci_search(self):
        print("%s is source list, %s is key"%(self.g_list, self.g_key))
        list = copy.copy(self.g_list)
        result = Demo_fibonacci_search.fibonacci_search(list, self.g_key)
        print("fibonacci search: ",result)
        write_line(0)

    # 哈希查找
    def demo_hash_search(self):
        print("%s is source list, %s is key"%(self.g_list, self.g_key))
        hashLength = len(self.g_list) + 1
        hash = {}
        for i in self.g_list:
            Demo_hash_search.insertHash(hash, hashLength, i)
        result = Demo_hash_search.searchHash(hash, hashLength, self.g_key)
        print("hash search: ",result)
        write_line(0)

    # 插值查找
    def demo_interpolation_search(self):
        print("%s is source list, %s is key"%(self.g_list, self.g_key))
        result = Demo_interpolation_search.interpolation_search(self.g_list, self.g_key)
        print("interpolation search: ",result)
        write_line(0)

    # 顺序查找
    def demo_sequential_search(self):
        print("%s is source list, %s is key"%(self.g_list, self.g_key))
        result = Demo_sequential_search.sequential_search(self.g_list, self.g_key)
        print("sequential search: ",result)

    # 查找中……
    def searching(self):
        print("Searching...")
        write_line(1)
        self.demo_bTree_search()
        self.demo_binary_search()
        self.demo_binary_tree_search()
        self.demo_block_search()
        self.demo_fibonacci_search()
        self.demo_hash_search()
        self.demo_interpolation_search()
        self.demo_sequential_search()
        write_line(1)

if __name__ == "__main__":
    d_sort = Demo_Sort()
    d_sort.sorting()

    d_search = Demo_Search()
    d_search.searching()
