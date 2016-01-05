# -*- coding: utf-8 -*-

# 冒泡排序
def bubble_sort(arry):
    n = len(arry)                   #获得数组的长度
    for i in range(n):
        for j in range(1,n-i):
            if  arry[j-1] > arry[j] :       #如果前者比后者大
                arry[j-1],arry[j] = arry[j],arry[j-1]      #则交换两者
    return arry
	

# 选择排序
def select_sort(arry):
    n = len(arry)
    for i in range(0,n):
        min = i                             #最小元素下标标记
        for j in range(i+1,n):
            if arry[j] < arry[min] :
                min = j                     #找到最小值的下标
        arry[min],arry[i] = arry[i],arry[min]   #交换两者
    return arry
	

# 插入排序
def insert_sort(arry):
    n = len(arry)
    for i in range(1,n):
        if arry[i] < arry[i-1]:
            temp = arry[i]
            index = i           #待插入的下标
            for j in range(i-1,-1,-1):  #从i-1 循环到 0 (包括0)
                if arry[j] > temp :
                    arry[j+1] = arry[j]
                    index = j   #记录待插入下标
                else :
                    break
            arry[index] = temp
    return arry
	
	
# 希尔排序
def shell_sort(arry):
    n = len(arry)
	#初始步长 , 用round四舍五入取整
    gap = round(n/2)
    while int(gap) > 0 :
		#每一列进行插入排序 , 从gap 到 n-1
        for i in range(int(gap),n):       
            temp = arry[i]
            j = i
            while ( j >= int(gap) and arry[j-int(gap)] > temp ):
				#插入排序
                arry[j] = arry[j-int(gap)]
                j = j - int(gap)
            arry[j] = temp
        #重新设置步长
	gap = round(int(gap)/2)
    return arry
	
	
# 归并排序
def merge_sort(arry):
    if len(arry) <= 1 : return arry
    num = int(len(arry)/2)       #二分分解
    left = merge_sort(arry[:num])
    right = merge_sort(arry[num:])
    return merge(left,right)    #合并数组

def merge(left,right):
    '''合并操作，
    将两个有序数组left[]和right[]合并成一个大的有序数组
	'''
    l,r = 0,0           #left与right数组的下标指针
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
	
	
# 快速排序
def quick_sort(arry):
    return qsort(arry,0,len(arry)-1)

def qsort(arry,left,right):
    #快排函数，arry为待排序数组，left为待排序的左边界，right为右边界
    if left >= right : return arry
    key = arry[left]     #取最左边的为基准数
    lp = left           #左指针
    rp = right          #右指针
    while lp < rp :
        while arry[rp] >= key and lp < rp :
            rp -= 1
        while arry[lp] <= key and lp < rp :
            lp += 1
        arry[lp],arry[rp] = arry[rp],arry[lp]
    arry[left],arry[lp] = arry[lp],arry[left]
    qsort(arry,left,lp-1)
    qsort(arry,rp+1,right)
    return arry
	
	
# 堆排序
def heap_sort(arry) :
    n = len(arry)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(arry,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        arry[end],arry[0] = arry[0],arry[end]
        max_heapify(arry,0,end-1)
    return arry


#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(arry,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and arry[child] < arry[child+1] :
            child = child+1             #取较大的子节点
        if arry[root] < arry[child] :     #较大的子节点成为父节点
            arry[root],arry[child] = arry[child],arry[root]     #交换
            root = child
        else :
            break