#python3 <file >fileout

import sys
from collections import defaultdict
cols=frozenset
def parser():
    IN=sys.stdin
    C=int(next(IN))
    for c in range(C):
        K=int(next(IN))#colors
        problem={}
        colors={}
        problem['c']=colors
        prim=0#index primay color
        for k in range(K):
            line=next(IN).strip().split()
            if len(line)==2:
                colors[(line[0])]=cols([prim])
                prim+=1
            else:
                colors[line[0]]=cols(x for i in line[2:] for x in colors[i]  )
        G=int(next(IN))
        problem['ng']=G
        galaxies=defaultdict(dict)
        for g in range(G):
            E=int(next(IN))
            for e in range(E):
                color,time=next(IN).strip().split()
                galaxies[g][problem['c'][color]]=int(time)
        problem['g']=galaxies
        W=int(next(IN))
        wormholes=defaultdict(list)
        for w in range(W):
            c,g1,g2=next(IN).strip().split()
            wormholes[int(g1)].append((int(g2),problem['c'][c]) )
        problem['w']=wormholes
        yield problem

class node:
    def __init__(self,problem,galaxy=0,BC=cols(),time=0):
        self.problem=problem
        self.time=time
        self.galaxy=galaxy
        self.buy_color=BC#colors than you could get in the past/now:cost
    def children(self):
        BC=self.BC.copy()
        for i,j in self.problem['g'].items():
            if (i not in BC) or (i in BC and BC[i]>j):
                BC[i]=j
                continue
        U=set().union(BC)
        for ng,c in self.problem['w'][self.galaxy]:
            if c.issubset( U):
                time=self.time+self.time_gather(c)
                BC2={}
                for i,j in ( (i.difference(c),j) for (i,j) in BC.items()):

                    BC2[i]=min(j,BC2[i]) if i in BC2 else j
                yield node(self.problem,ng ,BC2,time)
    def time_gather(self,c):
        pass

class node2:
    def __init__(self,problem,galaxy=0,BC=cols(),time=0):
        self.problem=problem
        self.time=time
        self.galaxy=galaxy
        self.buy_color=BC#colors than you have
    def __repr__(self):
        return 'g:%s,t:%s,c:%s'%(self.galaxy,self.time,self.buy_color)
    def __hash__(self):
        return hash((self.galaxy,self.buy_color))
    def moves(self):
        for color,time in self.problem['g'][self.galaxy].items():#,gather time     
            #print(color,self.buy_color)
            if color.issubset(self.buy_color):
                continue
            else:

                yield self.append(color,time)
        for (g2,c) in self.problem['w'][self.galaxy]:
            #print('sdf',c,self.buy_color)
            if self.buy_color.issuperset(c):
                
                yield self.move(c,g2)
    def append(self,color,time):
        return node2(self.problem,self.galaxy,cols(self.buy_color.union(color)),time+self.time)
    def __eq__(self,other):
        return self.galaxy==other.galaxy and self.buy_color==other.buy_color
    

    def move(self,c,g2):
        BC=cols(self.buy_color.difference(c))

        return node2(self.problem,g2,BC,self.time)
class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)


class PriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and the Stack classes. This is designed for drop-in replacement for
    those two classes. The caller has to provide a priority function, which
    extracts each item's priority.
    """
    def  __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction      # store the priority function
        PriorityQueue.__init__(self)        # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))


import heapq
h=lambda x:(x.time,-len(x.buy_color))
def found(node):
    p=PriorityQueueWithFunction(h)
    p.push(node)
    cont=True
    seeGalaxies={0:0}
    seen={}
    nG=(node.problem['ng'])
    while cont and not(p.isEmpty()):
        #print(node,node.galaxy)
        node=p.pop()
        if node not in seen or (node.time<seen[node]):
            seen[(node)]=node.time
        else:
            continue
        
        #cont=0#if dont move we 've finished
        for i in list(node.moves()):
        
            p.push(i)
           
            if i.galaxy not in seeGalaxies or seeGalaxies[i.galaxy]>i.time:
                seeGalaxies[(i.galaxy)]=i.time 
            cont=1
            if len(seeGalaxies)==nG:
                cont=False
                break
    #print(seeGalaxies)
    return ' '.join(map(str,((-1  if i not in seeGalaxies else seeGalaxies[i]) for i in range(nG))))
case='Case #%s: %s'
for c,i in enumerate(parser()):
    from pprint import pprint
    #pprint(i)
    print(case%(c+1,found(node2(i) ) ))
    pass
