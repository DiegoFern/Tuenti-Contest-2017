import os
from scipy import misc
from collections import Counter
a4=list(open('/tmp/p4','rb'))
a1=list(open('/tmp/p1','rb'))
def create_Im(*xs):
    F=open('/tmp/p','wb')
    for i in xs:
        F.write(i)
    F.close()
    os.system('google-chrome /tmp/p')
b=misc.imread('/tmp/p4')
b.shape[1]/3
b[:,1/3*b.shape[1]:b.shape[1]*3/4+15,:]=b[:,1/3*b.shape[1]:b.shape[1]*3/4+15:,:][:,::-1]
misc.imshow(b)


