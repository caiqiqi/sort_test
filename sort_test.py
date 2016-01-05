# -*- coding: utf-8 -*-

# from timeit import timeit as timeit
import time
import random
# 导入自己写的sort.oy
import sort


# 生成一个从1到1000的list
ls = list()
for i in range(1000):
	ls.append(i)

	

# 分别用几种排序算法对其排序
# 排序之前，用random.shuffle将其打乱

# 冒泡排序
random.shuffle(ls)
time_start = time.clock()
sort.bubble_sort(ls)
print ("冒泡排序用时: % s"  %(time.clock() - time_start) )

# 选择排序
random.shuffle(ls)
time_start = time.clock()
sort.select_sort(ls)
print ("选择排序用时: % s"  %(time.clock() - time_start) )

# 插入排序
random.shuffle(ls)
time_start = time.clock()
sort.insert_sort(ls)
print ("插入排序用时: % s"  %(time.clock() - time_start) )

# 希尔排序
random.shuffle(ls)
time_start = time.clock()
sort.shell_sort(ls)
print ("希尔排序用时: % s"  %(time.clock() - time_start) )

# 归并排序
random.shuffle(ls)
time_start = time.clock()
sort.merge_sort(ls)
print ("归并排序用时: % s"  %(time.clock() - time_start) )

# 快速排序
random.shuffle(ls)
time_start = time.clock()
sort.quick_sort(ls)
print ("快速排序用时: % s"  %(time.clock() - time_start) )

# 堆排序
random.shuffle(ls)
time_start = time.clock()
sort.heap_sort(ls)
print ("堆排序用时: % s"  %(time.clock() - time_start) )