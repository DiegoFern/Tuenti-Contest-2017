#########

#python3 <TestInput >outfile
import sys
case= "Case #%s: %s"

INP=sys.stdin
def value(rolls):
    score=[]
    frame=0
    sc=0
    while rolls:
        frame+=1
        if frame==10:
            sc+=sum(rolls)
            score.append(sc)
            rolls=[]
            continue
        r1=rolls.pop(0)
        
        if r1==10:
            sc+=10+rolls[1]+rolls[0]
            score.append(sc)
            continue
        r2=rolls.pop(0)
        if r1+r2==10:
            sc+=r1+r2+rolls[0]
            score.append(sc)
            continue
        sc+=r1+r2
        score.append(sc)
    return score
C=int(next(INP))
for c in range(C):
    next(INP)
    rolls=list(map(int,next(INP).strip().split()))
    print(case%(c+1,' '.join(map(str,value(rolls)) )))
