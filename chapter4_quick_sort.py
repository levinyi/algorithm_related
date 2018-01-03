
def sum2(alist):
	if len(alist) == 0:
		pass
	if len(alist) == 1:
		return alist
	else:
		for i in alist:
			return alist[0]+ sum2(alist[1:])

print(sum2([2,4,6]))
