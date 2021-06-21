import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
sock.listen(3)
clients_sock, address=sock.accept()
print('Connection from: '+str(address[0]))
while True:
	data=clients_sock.recv(1024)
	data=data.decode('utf-8')
	print(str(address[0])+': '+data)
