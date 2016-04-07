
import io
import cv2
import numpy as np
from PIL import Image

class Camera():

	def __init__(self, camSequence=0):
		self.camera = cv2.VideoCapture(camSequence)
		print "video capture initialized"

	def read(self):
		self.buffer = io.BytesIO()
		retval, frame = self.camera.read()

		if retval:
			img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			jpg = Image.fromarray(img)
			jpg.save(self.buffer, 'JPEG')
		return self.buffer
		
	def close(self):
		self.camera.release()
		print "camera stream closed"