#!/usr/bin/python

'''
this application is motion jpeg streaming server.
'''

import os
import sys
import cv2
import cam.cam
import httplib
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler

def main():
	global stream

	# default configure
	ip = "127.0.0.1"
	port = 8080

	if len(sys.argv) is 2:
		ip = str(sys.argv[1])

	# usb camera mode [USB_CAM, PI_CAM]
	stream = cam.cam.Camera(cam.cam.USB_CAM)

	# http server
	try:
		httpd = SocketServer.TCPServer((ip, port), MjpegServerHandler)
		httpd.serve_forever()
		print "%s:%s server started" % (ip, port)
	except KeyboardInterrupt:
		stream.close()
		httpd.server_close()

class MjpegServerHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(httplib.OK)
		self.send_header("Content-type", "multipart/x-mixed-replace;boundary=boundarytag")
		self.end_headers()
			
		while True:
			self.frame = stream.read()
			self.wfile.write("--boundarytag")
			self.send_header("Content-type", "image/jpeg")
			self.send_header("Content-Length", len(self.frame.getvalue()))
			self.end_headers()
			self.wfile.write(self.frame.getvalue())

if __name__ == '__main__':
	main()