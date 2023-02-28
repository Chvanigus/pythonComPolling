""" Клиентский скрипт опроса весовой"""
import socket

s = socket.socket()
host = '192.168.6.38'
port = 12345

s.connect((host, port))
data = s.recv(1024)
print(data)
s.close()
