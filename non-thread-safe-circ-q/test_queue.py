from queue import Queue


if __name__ == '__main__':
	x = Queue(3)
	assert x.pop() == None
	x.push(1)
	x.push(2)
	x.push(3)
	x.push(4) # this call shuold fail
	print(x.arr)
	assert x.pop() == 1
	assert x.pop() == 2
	assert x.pop() == 3
	assert x.pop() == None