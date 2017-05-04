def conc(s,c,d):
    c-=c%2
    if c>=12 and s>1:
        s-=s%2
        return s+c+d
    if c>=12 :
        c-=c%4
        return s+c+d
    #c<12
    if c in (8,6,4) and s>=2 :#(2,10,0)y (2,8,0) possible
        s-=s%2
        return s+c+d
    if c<4:
        return 0
    if c in (8,) and s<=1:
        return 8+d
        
    if c in (4,) and s<=1:
        return 8+d-d%2


