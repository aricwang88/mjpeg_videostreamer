from BaseHTTPServer import BaseHTTPRequestHandler
import SocketServer
import os
import shutil
import time
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import httplib
from PIL import Image
import StringIO

IP = "10.64.69.240"
PORT = 8080

class MjpegServerHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):

		camera = picamera.PiCamera()
		#camera.resolution = (320, 240)

		try:
			self.send_response(httplib.OK)
			self.send_header("Content-type", "multipart/x-mixed-replace;boundary=boundarytag")
			self.end_headers()

			#buffered stream (BytesIO -> BufferedIOBase -> IOBase)
			stream = io.BytesIO()  

			#Capture images continuously from the camera as an infinite iterator.
			for foo in camera.capture_continuous(stream,'jpeg'):

				self.wfile.write("--boundarytag")
				self.send_header("Content-type", "image/jpeg")
				self.send_header("Content-Length", len(stream.getvalue()))
				self.end_headers()
				
				self.wfile.write(stream.getvalue())

				#start of stream
				stream.seek(0)		
          		stream.truncate()

		except KeyboardInterrupt:
			print "keboard interrupt"
		finally:
			camera.close()
		
if __name__ == '__main__':
	Handler = MjpegServerHandler
	httpd = SocketServer.TCPServer((IP, PORT), Handler)
	httpd.serve_forever()
	print "server at port", PORT
