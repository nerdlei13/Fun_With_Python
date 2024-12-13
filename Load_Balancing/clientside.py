import http.server
import requests
import socketserver
import socket
import sys

# challenge: make this a more secure port
# https://docs.python.org/3/library/socketserver.html#socketserver.TCPServer
PORT = 7070
HOST = "localhost"
data = "testing"

# fix this to send multiple requests to server
#for i in range(10):
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")



print("Sent:     {}".format(data))
print("Received: {}".format(received))

