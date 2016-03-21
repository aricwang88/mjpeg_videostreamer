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

PORT = 8080

class MjpegServerHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		cap = cv2.VideoCapture(0)
		
		try:
			self.send_response(httplib.OK)
			self.send_header("Content-type", "multipart/x-mixed-replace;boundary=boundarytag")
			self.end_headers()
			
			while True:
				retval, frame = cap.read()
				retval, image = cv2.imencode('.jpg',frame)
				image_buff = image.tobytes()
				self.wfile.write("--boundarytag")
				self.send_header("Content-type", "image/jpeg")
				self.send_header("Content-Length", len(image_buff))
				self.end_headers()
				
				self.wfile.write(image_buff)
				time.sleep(0.1)
		except:
			raise
		cap.release()

if __name__ == '__main__':
	Handler = MjpegServerHandler
	httpd = SocketServer.TCPServer(("127.0.0.1", PORT), Handler)
	httpd.serve_forever()
	print "server at port", PORT
	