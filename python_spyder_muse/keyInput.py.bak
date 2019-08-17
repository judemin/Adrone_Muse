import socket
from select import select
import json
from pprint import pprint
import random
import sys
import pyautogui
import time

backup = ""

def progress(dat) : 
	pyautogui.keyDown('backspace')
	pyautogui.keyDown('backspace')
	pyautogui.keyDown('backspace')
	pyautogui.keyDown('backspace')
	for i in dat : 
		print("KeyPress : " + i);
		pyautogui.keyDown(i)
	pyautogui.press('enter')

def changeSignal(tmp) : 
	f = open("Dats.txt", 'w')
	f.write(str(tmp))
	f.close()

def testFile() :
	global backup
	f = open("Dats.txt", 'r')
	line = f.readline()
	val = line
	if(val != backup):
		print(line)
		progress(str(val))
		backup = val
	f.close()

changeSignal(50);
testFile();

while 1:
	time.sleep(0.1)
	testFile()

"""
sep = "\n"
HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])

s.listen(1)
conn, addr = s.accept()
print ("Connected by " ,  addr)
while 1:
	buf = ''
	while sep not in buf:
		buf += conn.recv(8).decode()
	num = int(buf);
	if num is -1 : 
		break;
	print ("Data : " , num)
	changeSignal(num)
	testFile()
	progress(str(num))
conn.close()
"""