#python3 <file >fileout

import sys
from math import *

case= "Case #%s: %s"
IN=sys.stdin

T=int(next(IN))
for t in range(T):
    next(IN)
    num_por=sum(map(int,str.strip(next(IN)).split()))
    print(case%(t+1,ceil(num_por/8)))
