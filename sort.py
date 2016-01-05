# -*- coding: utf-8 -*-

# ð������
def bubble_sort(arry):
    n = len(arry)                   #�������ĳ���
    for i in range(n):
        for j in range(1,n-i):
            if  arry[j-1] > arry[j] :       #���ǰ�߱Ⱥ��ߴ�
                arry[j-1],arry[j] = arry[j],arry[j-1]      #�򽻻�����
    return arry
	

# ѡ������
def select_sort(arry):
    n = len(arry)
    for i in range(0,n):
        min = i                             #��СԪ���±���
        for j in range(i+1,n):
            if arry[j] < arry[min] :
                min = j                     #�ҵ���Сֵ���±�
        arry[min],arry[i] = arry[i],arry[min]   #��������
    return arry
	

# ��������
def insert_sort(arry):
    n = len(arry)
    for i in range(1,n):
        if arry[i] < arry[i-1]:
            temp = arry[i]
            index = i           #��������±�
            for j in range(i-1,-1,-1):  #��i-1 ѭ���� 0 (����0)
                if arry[j] > temp :
                    arry[j+1] = arry[j]
                    index = j   #��¼�������±�
                else :
                    break
            arry[index] = temp
    return arry
	
	
# ϣ������
def shell_sort(arry):
    n = len(arry)
	#��ʼ���� , ��round��������ȡ��
    gap = round(n/2)
    while int(gap) > 0 :
		#ÿһ�н��в������� , ��gap �� n-1
        for i in range(int(gap),n):       
            temp = arry[i]
            j = i
            while ( j >= int(gap) and arry[j-int(gap)] > temp ):
				#��������
                arry[j] = arry[j-int(gap)]
                j = j - int(gap)
            arry[j] = temp
        #�������ò���
	gap = round(int(gap)/2)
    return arry
	
	
# �鲢����
def merge_sort(arry):
    if len(arry) <= 1 : return arry
    num = int(len(arry)/2)       #���ַֽ�
    left = merge_sort(arry[:num])
    right = merge_sort(arry[num:])
    return merge(left,right)    #�ϲ�����

def merge(left,right):
    '''�ϲ�������
    ��������������left[]��right[]�ϲ���һ�������������
	'''
    l,r = 0,0           #left��right������±�ָ��
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
	
	
# ��������
def quick_sort(arry):
    return qsort(arry,0,len(arry)-1)

def qsort(arry,left,right):
    #���ź�����arryΪ���������飬leftΪ���������߽磬rightΪ�ұ߽�
    if left >= right : return arry
    key = arry[left]     #ȡ����ߵ�Ϊ��׼��
    lp = left           #��ָ��
    rp = right          #��ָ��
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
	
	
# ������
def heap_sort(arry) :
    n = len(arry)
    first = int(n/2-1)       #���һ����Ҷ�ӽڵ�
    for start in range(first,-1,-1) :     #��������
        max_heapify(arry,start,n-1)
    for end in range(n-1,0,-1):           #���ţ��������ת������������
        arry[end],arry[0] = arry[0],arry[end]
        max_heapify(arry,0,end-1)
    return arry


#���ѵ��������ѵ�ĩ���ӽڵ���������ʹ���ӽڵ���ԶС�ڸ��ڵ�
#startΪ��ǰ��Ҫ�������ѵ�λ�ã�endΪ�����߽�
def max_heapify(arry,start,end):
    root = start
    while True :
        child = root*2 +1               #�����ڵ���ӽڵ�
        if child > end : break
        if child+1 <= end and arry[child] < arry[child+1] :
            child = child+1             #ȡ�ϴ���ӽڵ�
        if arry[root] < arry[child] :     #�ϴ���ӽڵ��Ϊ���ڵ�
            arry[root],arry[child] = arry[child],arry[root]     #����
            root = child
        else :
            break