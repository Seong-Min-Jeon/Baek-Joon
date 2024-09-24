import sys
ip=sys.stdin.readline
for _ in range(int(ip())):
    l=[]
    s=ip().rstrip()
    for e in s:
        if(e=='('): l.append(e)
        elif(e==')'):
            if(len(l)>0 and l[-1]=='('): l.pop()
            else: l.append(e); break
    if(len(l)==0): print('YES')
    else: print('NO')