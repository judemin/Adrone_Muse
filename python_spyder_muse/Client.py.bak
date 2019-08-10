import socket

sep = "\n"
val = "";
num = 0;
HOST = '127.0.0.1'                
PORT = 50007              

HOST = input("Enter IP : ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
	num = int(input("Enter a Signal : "))
	val = str(num) + sep
	s.send(val.encode())
	print ("Sending Complete!")
s.close()