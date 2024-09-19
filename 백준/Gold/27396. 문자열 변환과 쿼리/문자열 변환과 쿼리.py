import sys

def p(s,d:dict):
    for e in s:
        if(e in d):
            print(d.get(e), end='')
        else:
            print(e, end='')
    print(end='\n')

ip=sys.stdin.readline
s,n=ip().split()
d=dict()
for _ in range(int(n)):
    a=ip().strip()
    if(a=='2'):
        p(s,d.copy())
    else:
        x,f,t=a.split()
        if(f==t): continue
        if(f in d.values()):
            for k in d.keys():
                if(d[k]==f):
                    d[k]=t
            if(f not in d.keys()):
                d[f]=t
        elif(f in d.keys()):
            pass
        else:
            d[f]=t