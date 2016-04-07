
import camera

camera = camera.Camera(False)

while True:
	frame = camera.read()
	print len(frame.getvalue())
