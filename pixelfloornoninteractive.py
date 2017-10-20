#!/usr/bin/env python3
import socket
import fileinput

#socket connection
HOST = '10.90.154.80' # IP addres of raspberry pi (?)
PORT = 51234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
send = sock.send
# end socket connection

with fileinput.input() as f_input:  # This gets the piped data for you
    for line in f_input:
        # print(line, end="") # for debugging code (comment socket connection if want to enable)
        parts = line.split()
        # print(parts)
        # print(int(parts[1]))
        # print(int(parts[2]))

        #print("PX %d %d %s" %(int(parts[1]), int(parts[2]), parts[3]))
        send("PX %d %d %s" %(int(parts[1]), int(parts[2]), parts[3]))
