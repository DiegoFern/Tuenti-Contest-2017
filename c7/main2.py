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
    floors=sorted(floorsA.union(floorsB))

def dist()
def minimun_years(floors,i,j,shorts):
    #minimo de años entre la planta floors[i] a j sin retroceder
    return min(min((t+minimun_years(floors,i+1:e,j,shorts  ) for t,d in shorts ),
            dist(floors[i],floors[i+1])+minimun_year(floors,floors[i+1],j,shorts))

            
case="Case #%s: %s"
C=int(next(sys.stdin))
for c in range(C):
    F,S=tuple(map(int,next(sys.stdin).split()))
    linesTower=[ next(sys.stdin)
                    for s in range(S)]
    print(case%(c+1,createGraph(linesTower,F)))
