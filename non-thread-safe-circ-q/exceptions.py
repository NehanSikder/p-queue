

class QueueInitialiaztionError(Exception):

	def __init__(self, message = "Unable to create queue since size arg needs to be provided and has to be of value > 0"):
		self.message = message
		super().__init__(self.message)


class QueueFullError(Exception):

	def __init__(self, message = "Unable to add to queue since queue is full"):
		self.message = message
		super().__init__(self.message)


class QueueEmptyError(Exception):

	def __init__(self, message = "Unable to read from queue since queue is empty"):
		self.message = message
		super().__init__(self.message)
