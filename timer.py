import datetime

class Timer:
	def __init__(self):
		self._start_time = None
		self._end_time = None

	def start(self):
		self._start_time = datetime.datetime.now()

	def end(self):
		self._end_time = datetime.datetime.now()

	def elapsed(self):
		return (self._end_time - self._start_time).total_seconds()