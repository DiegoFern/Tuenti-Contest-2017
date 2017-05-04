#python3 <file >fileout
from networkx import DiGraph,single_source_dijkstra
import networkx as nx
import sys
def createGraph(linesTower,F):
    G=DiGraph()
    floorsA={1,F}
    floorsB={F,1}
    for a,b,c in map(lambda line:line.strip().split(),linesTower):
        a,b,c=int(a),int(b),int(c)
        if not( a in G) or not(b in G[a]) or G[a][b]['w']>c:
            G.add_edge(a,b,w=c)
        floorsA.add(a)
        floorsB.add(b)

    def h(x,y):
        return max(0,(y*(y-1)-x*(x-1))/2)
    for i in floorsA:
        for j in floorsA.union(floorsB):
            if i<j:
                G.add_edge(j,i,w=0)
                
            else:
                w=int(-(j*(j-1)-i*(i-1))/2)
                #j,i=i,j
                if not( j in G) or not(i in G[j]) or G[j][i]['w']>w:
                    G.add_edge(j,i,w=w)
    p=nx.dijkstra_path(G,1,F,weight='w')
    l=0
    
    for a,b in zip(p,p[1:]):
        l+=G[a][b]['w']
    return l
case="Case #%s: %s"
C=int(next(sys.stdin))
for c in range(C):
    F,S=tuple(map(int,next(sys.stdin).split()))
    linesTower=[ next(sys.stdin)
                    for s in range(S)]
    print(case%(c+1,createGraph(linesTower,F)))    
