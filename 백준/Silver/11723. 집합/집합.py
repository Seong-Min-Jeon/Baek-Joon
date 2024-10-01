import sys
i=sys.stdin.readline
s=set()
for _ in range(int(i())):
    m=i().strip()
    if(' ' in m):
        a,b=m.split()
        b=int(b)
        if(a=='add'): s.add(b)
        if(a=='remove' and (b in s)): s.remove(b)
        if(a=='check'): print(1 if(b in s) else 0)
        if(a=='toggle' and (b in s)): s.remove(b)
        elif(a=='toggle'): s.add(b)
    if(m=='all'): s={i for i in range(1,21)}
    if(m=='empty'): s.clear()