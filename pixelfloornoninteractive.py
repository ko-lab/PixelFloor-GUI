#!/usr/bin/env python3
import socket
import fileinput

#socket connection
HOST = 'xx.xx.xx.xx' # IP addres of raspberry pi (?)
PORT = 51234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
send = sock.send
# end socket connection 

with fileinput.input() as f_input:  # This gets the piped data for you
    for line in f_input:
        # print(line, end="") # for debugging code (comment socket connection if want to enable)
        send(line)
