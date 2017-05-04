#python3 <file >fileout

import sys
IN=sys.stdin

def evaluate(c,vertex):
    r=2**60
    find=False
    for i in range(len(vertex)-2):
        if vertex[i]>r:
            break
        for j in range(i+1,len(vertex)-1):
            if vertex[j]>r:
                break
            if vertex[j+1]<vertex[j]+vertex[i] and vertex[j+1]+vertex[j]+vertex[i]<r:
                r= sum(( vertex[j+1],vertex[j],vertex[i]))
    if r==2**60:
        return case%(c+1,'IMPOSSIBLE')
    else:
        return case%(c+1,r)

case='Case #%s: %s'

N=int(next(IN))
for c,line in enumerate(IN):
    vertex=sorted(map(int,line.strip().split()[1:]))
    print(evaluate(c,vertex))

