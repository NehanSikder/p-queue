
from exceptions import QueueFullError, QueueEmptyError

class Queue():


	def __init__(self, size):
		#TODO make size parameter mandatory
		#TODO make size parameter is > 0
		self.size = size
		self.arr = [None] * self.size
		self.read_index = 0
		self.write_index = 0


	def push(self, val):
		if self.arr[self.write_index] != None:
			raise QueueFullError
		self.arr[self.write_index] = val
		self.write_index = self.write_index + 1
		if self.write_index == self.size:
			self.write_index = 0


	def pop(self):
		if self.arr[self.read_index] == None:
			raise QueueEmptyError
		res = self.arr[self.read_index]
		self.arr[self.read_index] = None
		self.read_index = self.read_index + 1
		if self.read_index == self.size:
			self.read_index = 0
		return res