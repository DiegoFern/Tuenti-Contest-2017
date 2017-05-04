#python3
import sys
IN=sys.stdin

case='Case #%s: %s'
from math import *
next(IN)
for i,p in enumerate(map(int,IN)):
    print(case%(i+1,ceil(log2(p+1))))
