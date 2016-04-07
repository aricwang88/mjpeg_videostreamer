import io
import copy
from picamera import PiCamera

class Camera():
	
	def __init__(self):
		self.camera = PiCamera()
		self.buffer = io.BytesIO()
		self.stream = self.camera.capture_continuous(self.buffer, "jpeg")

	def read(self):
		self.retbuffer = copy.deepcopy(self.stream.next())
		print "a"
		self.buffer.seek(0)
		self.buffer.truncate()
		return self.retbuffer

	def close(self):
		self.camera.close()
