'''
this application is motion jpeg streaming server.
'''

from BaseHTTPServer import BaseHTTPRequestHandler
import SocketServer
import os
import shutil
import time
import numpy as np
import cv2
import httplib
from timer import Timer
from fps import Fps

IP = "127.0.0.1"
PORT = 8080

class MjpegServerHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		fps = Fps()

		init_time = Timer()
		init_time.start()
		cap = cv2.VideoCapture(0)
		try:
			init_time.end()
			print "initialization time : " + str(init_time.elapsed()) + " elapsed"
			self.send_response(httplib.OK)
			self.send_header("Content-type", "multipart/x-mixed-replace;boundary=boundarytag")
			self.end_headers()
			fps.start()
			
			while True:
				t = Timer()
				retval, frame = cap.read()
				
				t.start()
				retval, image = cv2.imencode('.jpg',frame)
				t.end()
				print "frame encoding time : " + str(t.elapsed()) + " elapsed"

				image_buff = image.tobytes()
				self.wfile.write("--boundarytag")
				self.send_header("Content-type", "image/jpeg")
				self.send_header("Content-Length", len(image_buff))
				self.end_headers()
				
				self.wfile.write(image_buff)
				fps.increase()
		except KeyboardInterrupt:
			print "keboard interrupt"
		finally:
			fps.end()
			cap.release()
			print fps.fps()
		
if __name__ == '__main__':
	Handler = MjpegServerHandler
	httpd = SocketServer.TCPServer((IP, PORT), Handler)
	httpd.serve_forever()
	print "server at port", PORT