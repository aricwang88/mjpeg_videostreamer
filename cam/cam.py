import usbcam

USB_CAM = 1
PI_CAM = 2

class Camera():
	def __init__(self, camType=1):
		if camType == PI_CAM:
			import picam
			self.camera = picam.Camera()
			print "picamera initialized"
		else:
			self.camera = usbcam.Camera()
			print "usbcamera initialized"

	def read(self):
		return self.camera.read()

	def close(self):
		self.camera.close()
