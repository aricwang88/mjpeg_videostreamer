import timer

class Fps(timer.Timer):
	def __init__(self):
		self._frames = 0

	def increase(self):
		self._frames = self._frames + 1

	def fps(self):
		return self._frames / self.elapsed()