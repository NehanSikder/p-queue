from queue import Queue
from exceptions import QueueFullError, QueueEmptyError


if __name__ == '__main__':
	x = Queue(3)
	try:
		x.pop()
	except QueueEmptyError as e:
		print(e.message)

	x.push(1)
	x.push(2)
	x.push(3)
	
	try:
		x.push(4) # this call shuold fail
	except QueueFullError as e:
		print(e.message)

	


	assert x.pop() == 1
	assert x.pop() == 2
	assert x.pop() == 3


	try:
		x.pop()
	except QueueEmptyError as e:
		print(e.message)