# -*- coding: utf-8 -*-

# from timeit import timeit as timeit
import time
import random
# �����Լ�д��sort.oy
import sort


# ����һ����1��1000��list
ls = list()
for i in range(1000):
	ls.append(i)

	

# �ֱ��ü��������㷨��������
# ����֮ǰ����random.shuffle�������

# ð������
random.shuffle(ls)
time_start = time.clock()
sort.bubble_sort(ls)
print ("ð��������ʱ: % s"  %(time.clock() - time_start) )

# ѡ������
random.shuffle(ls)
time_start = time.clock()
sort.select_sort(ls)
print ("ѡ��������ʱ: % s"  %(time.clock() - time_start) )

# ��������
random.shuffle(ls)
time_start = time.clock()
sort.insert_sort(ls)
print ("����������ʱ: % s"  %(time.clock() - time_start) )

# ϣ������
random.shuffle(ls)
time_start = time.clock()
sort.shell_sort(ls)
print ("ϣ��������ʱ: % s"  %(time.clock() - time_start) )

# �鲢����
random.shuffle(ls)
time_start = time.clock()
sort.merge_sort(ls)
print ("�鲢������ʱ: % s"  %(time.clock() - time_start) )

# ��������
random.shuffle(ls)
time_start = time.clock()
sort.quick_sort(ls)
print ("����������ʱ: % s"  %(time.clock() - time_start) )

# ������
random.shuffle(ls)
time_start = time.clock()
sort.heap_sort(ls)
print ("��������ʱ: % s"  %(time.clock() - time_start) )