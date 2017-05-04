#python3 main.py inputFile numberLines >outFile
import re
regex=re.compile('\s*(\d+)\s*')
import sys
_,input,lines=(sys.argv)
IN=open(input,'r',encoding='utf-16le')
case="Case #%s: %s"
C=int(lines)
next(IN)
for c in range(int(C)):
    line=next(IN)[:-1]
    s=regex.match(line)
    if s and s.span()[1]==len(line):
        a,b=s.span()
        print(case%(c+1,hex(int(line[a:b]))[2:]))
    else:
        print(case%(c+1,'N/A'))
    #except:
    #    print(case%(c+1,'N/A'))

