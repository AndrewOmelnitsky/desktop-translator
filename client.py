import cv2
import numpy as np
import socket
import sys
import pickle
import struct
from PIL import ImageGrab as ig

# cap = cv2.VideoCapture(1)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8128
clientsocket.connect(('192.168.0.7', PORT))

while True:
    # ret,frame = cap.read()
    screen = ig.grab(bbox=None)# (50,50,3000,640)
    data = pickle.dumps(cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
    clientsocket.sendall(struct.pack("L", len(data)) + data)
