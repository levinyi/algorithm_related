#!/usr/bin/python3

def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print selectionSort([3,6,9,44,77,67,45,8,7])
