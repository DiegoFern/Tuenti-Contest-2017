#python3 <file >fileout

import getpass
import sys
import telnetlib

HOST = "52.49.91.111"
tn = telnetlib.Telnet(HOST,port=3456)

tn.read_until("bro")

tn.write("ls\n")
tn.write("exit\n")

