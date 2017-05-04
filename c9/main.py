#python3 <file >fileout
class scalectric:
    def __init__(self,pos,sentido,s,c,d,depth=0,path=set()):
        self.s=s
        self.c=c
        self.path=path
        self.d=d
        self.pos=pos
        self.depth=depth
        self.sentido=sentido
    def reset(self):
        self.pos=(0,0)
        self.sentido=(1,0)
    def __repr__(self):
        return '{ps:%s,st=%s}'%(self.pos,self.sentido)
    def rigth(self):
        
        pos=(self.pos[0]+self.sentido[0],self.pos[1]+self.sentido[1])
        path=self.path.union((pos,))
        sentido=(self.sentido[1],-self.sentido[0])
        pos=(pos[0]+sentido[0],pos[1]+sentido[1])

        return scalectric(pos,sentido,self.s,self.c-1,self.d,self.depth+1,path) 
    def left(self):
        pos=(self.pos[0]+self.sentido[0],self.pos[1]+self.sentido[1])
        path=self.path.union((pos,))

        sentido=(-self.sentido[1],self.sentido[0])
        pos=(pos[0]+sentido[0],pos[1]+sentido[1])
        return scalectric(pos,sentido,self.s,self.c-1,self.d,self.depth+1,path)
    def forwad(self):
        path=self.path.union(((self.pos[0]+self.sentido[0],self.pos[1]+self.sentido[1]),))
        pos=self.pos[0]+self.sentido[0]*2,self.pos[1]+self.sentido[1]*2
        return scalectric(pos,self.sentido,self.s-1,self.c,self.d,self.depth+1,path) 
    def forwad2(self):
        path=self.path.union(((self.pos[0]+2*self.sentido[0],self.pos[1]+2*self.sentido[1]),))
        pos=self.pos[0]+4*self.sentido[0],self.pos[1]+4*self.sentido[1]
        return scalectric(pos,self.sentido,self.s,self.c,self.d-1,self.depth+1,path)
    def isgoal(self):
        return (self.pos==(0,0) and 
        self.sentido==(1,0) and self.depth>0)
    def mov_legales(self):
        r=[]
        if ((self.pos[0]+self.sentido[0],self.pos[1]+self.sentido[1])   in self.path) or dist(self.pos)>self.c+self.s+2*self.d:
            return []
        if self.c>0:
            r.append(self.left())
            r.append(self.rigth())
        if self.d>0:
            r.append(self.forwad2())
        if self.s>0:
            r.append(self.forwad())
        return r
    def __hash__(self):
        return hash((self.depth,self.pos,self.sentido,self.d,self.c,self.pos))
    def __eq__(s,o):
        return s.c==o.c and s.s==o.s and s.d==o.d and s.pos==o.pos and s.sentido==o.sentido and s.path==o.path

def dist(x):
    (a,b)=x
    return (abs(a)+abs(b))/2
def allpath(s,c,d):
    scal=scalectric((0,0),(1,0),s,c,d)
    nodes=[scal]
    seen=set()
    better=0
    targets={}
    try:
        while nodes:
            node=nodes.pop()
            if node in seen or (node.c==0 and node.sentido!=(1,0)):
                continue
            seen.add(node)
            if node.isgoal() and (s-node.s,c-node.c,d-node.d) not in targets:
                targets[((s-node.s,c-node.c,d-node.d))]=node
                found.node=node
                continue
            nodes.extend(node.mov_legales())
    except:
        pass
    #s=set(targets)
    return targets
def found(scal):
    scal.c-=scal.c%2
    if scal.c<4:
        return 0

    nodes=[scal]
    seen=set()
    better=0
    while nodes:
        node=nodes.pop()
        if node in seen: #or (node.c==0 and node.sentido!=(1,0)):
            continue
        seen.add(node)
        if node.isgoal():
            better=max(better,node.depth)
            found.node=node
            continue
        nodes.extend(node.mov_legales())
    return better
def main():
    case= "Case #%s: %s"
    import sys
    IN=sys.stdin
    next(IN)
    i=0
    for line in (IN):
        i+=1
        s,c,d=tuple(map(int,line.strip().split()))
        print(case%(i,conc(s,c,d)))
def conc(s,c,d):
    c-=c%2
    if c>=12 and s>1:
        s-=s%2
        return s+c+d
    if c>=12 :
        c-=c%4
        return s+c+d
    #c<12
    if c in (10,8,6,4) and s>=2 :#(2,10,0)y (2,8,0) possible
        s-=s%2
        return s+c+d
    c-=c%4
    if c<4:
        return 0
    if c in (8,) and s<=1 :
        if d>0:
            return 8+d
        else:
            return 4
        
    if c in (4,) and s<=1:
        return 4+d-d%2
main()
