# telnet program example
import socket, select, string, sys,os,time
from PIL import Image
from scipy import misc,ndimage
def load_rev_photo(dire):

    A=misc.imread(dire)
    print(A.shape,dire)
    s=0
    for i in range(0,A.shape[1],40):
        if s%2==1:
            A[:,i:i+40,:]=A[:,i:i+40,:][:,::-1]
        else:
            pass
        s+=1
    return A
def media_color(M_I):
    return
    d={}
    for i in range(0,M_I.shape[1],54):
        for j in range(0,M_I.shape[1],53):
            d[i,j]=M_I[i:i+54,j:j+53].mean(axis=(0,1))
    print(d)


#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 3) :
        print 'Usage : python telnet.py hostname port'
        sys.exit()
     
    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(dir(s))
    s.settimeout(1000000)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host'
    j=0
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
        for sock in read_sockets:
            j+=1
            #incoming message from remote server
            if sock == s:
                data = sock.recv(2**30)
                if not data :
                    print 'Connection closed'
                    time.sleep(1)
                else :
                    #print data
                    #############
                    S=0
                    if len(data)>50:
                        
                        F=open('/tmp/p%s'%j,'wb')
                        while len(data)>50:

                            F.write(data)
                            F.flush()

                            data = sock.recv(2**30)
                            if len(data)>50:
                                os.system('google-chrome /tmp/p%s.jpg &'%j)
                        F.close()
                        print(data)
                        if 1!=j:
                            I=load_rev_photo('/tmp/p%s'%j)
                            print media_color(I)
                            #I=ndimage.percentile_filter(I,percentile=20,size=10)
                            misc.imsave('/tmp/p%s.jpg'%j,I)
                            os.system('google-chrome /tmp/p%s.jpg &'%j)

                        S+=1
                    print S
                    
                    sys.stdout.write(data)
                    
             
            #user entered a message
            else :
                if j!=1:
                    msg = sys.stdin.readline()
                    s.send(msg)
                else:
                    s.send('1')
