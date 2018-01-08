
def sum2(alist):
	if len(alist) < 2:
		return alist
	else:
		for i in alist:
			return alist[0]+ sum2(alist[1:])

# print(sum2([2,4,6]))

def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]
		return quicksort(less)+[pivot] +quicksort(greater)
print quicksort([10,5,2,3])
print quicksort([33,15,10])