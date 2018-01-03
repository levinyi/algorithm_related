#!/usr/bin python3
#recursion
# method1
def look_for_key(main_box):
	pile = main_box.make_a_pile_to_look_through()
	while pile is not empty:
		box = pile.grab_a_box()
		for item in box:
			if item.is_a_box():
				pile.append(item)
			elif item.is_a_key():
				print("found the key!")
# method2

def look_for_key(box):
	for item in box:
		if item.is_a_box():
			look_for_key(item)
		elif item.is_a_key():
			print("found the key")
# 每个递归函数都有两部分：基线条件（base case）和递归条件（recursive case）。递归条件指的是函数调用自己，而基线条件则是指的是函数不再调用自己，从而避免形成无限循环。
# 调用栈
def greet(name):
	print("hello ,"+name+"!")
	greet2(name)
	print("getting ready to say bye...")
	bye()
def greet2(name):
	print("how are you "+ name +"?")
def bye():
	print("ok,bye")
# 计算机使用一个栈来表示这些内存块，其中第二个内存块位于第一个内存块上面，执行完之后，栈顶的内存块被弹出。
# 递归调用栈

def fact(x):
	if x==1:
		return 1
	else:
		return x*fact(x-1)
# 调用栈可能很长，这将占用大量的内存