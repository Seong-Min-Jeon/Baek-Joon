import sys
ip=sys.stdin.readline
for _ in range(int(ip())):
    l=list(ip().strip())
    s,t,c='','',0
    for e in l:
        if(t==''): t=e; c+=1; continue
        if(e==t): c+=1
        else: s+=str(c)+t; t,c=e,1
    s+=str(c)+t
    print(s)