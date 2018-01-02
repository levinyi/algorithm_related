#/usr/bin/ python3
''' binary search algorithm'''
import sys
import os


def binary_search(alist,item):
	low = 0
	high  = len(alist) - 1
	while low < high:
		mid = (high + low)/2
		guess = alist[mid]
		if guess < item:
			low = mid+1
		if guess > item :
			high = mid + 1
		if guess == item:
			return mid
my_list = [1,3,5,7,9,10,12,14,15,17,34,45]

print binary_search(my_list,3)
