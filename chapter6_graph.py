#!/usr/bin/env python3
#广度优先搜索
graph = {}
graph["you"] = ["alice","bob","claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj","peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
	from collections import deque
	search_queue = deque()
	search_queue += graph["you"]
	searched = []

	while search_queue:
		person = search_queue.popleft()
		if person not in searched:
			if person_is_seller(person):
				print(person + " is a mango seller!")
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False

def person_is_seller(name):
	return name[-1] == 'm'

search("you")