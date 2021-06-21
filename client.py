import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip,port=input('Print ip:port ').split(':')
port=int(port)
sock.connect((ip,port))
while True:
	msg=input('Print message: ')
	sock.send(bytes(msg, 'utf-8'))