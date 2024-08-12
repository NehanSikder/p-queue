from queue import Queue
from exceptions import QueueFullError, QueueEmptyError, QueueInitialiaztionError


if __name__ == '__main__':

	try:
		x = Queue()
	except QueueInitialiaztionError as e:
		print(e.message)


	try:
		x = Queue(0)
	except QueueInitialiaztionError as e:
		print(e.message)


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