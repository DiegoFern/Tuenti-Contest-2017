'''
    Simple socket server using threads
'''
 
import socket
import sys
 
HOST = '52.49.91.111'   # Symbolic name, meaning all available interfaces
PORT = 3456 # Arbitrary non-privileged port
 
s = socket.socket()
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.connect((HOST, PORT))

except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
print 'Socket now listening'
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    recv= s.recv(100000)
    
    print recv
    s.send(raw_input('>').)
     
s.close()
