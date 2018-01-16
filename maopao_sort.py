# -*- coding: utf-8 -*-
# 冒泡排序
def msort(alist):
	number = len(alist) #5 总共有5个数
	# 先来排序第一趟
	print(alist,len(alist))
	for i in range(len(alist)-1):
		print i
		if alist[i] < alist[i+1]:
			alist[i],alist[i+1] = alist[i+1],alist[i]
			print alist
	# alist.pop()
	msort(alist)

msort([6,1,2,7,9,3,4,5,19,8])

