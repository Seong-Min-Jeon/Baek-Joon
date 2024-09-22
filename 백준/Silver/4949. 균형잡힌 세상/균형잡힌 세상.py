import sys
ip=sys.stdin.readline
while True:
    l=[]
    s=ip().rstrip()
    if(s=='.'): break
    for e in s:
        if(e=='(' or e=='['): l.append(e)
        elif(e==')'):
            if(len(l)>0 and l[-1]=='('): l.pop()
            else: l.append(e); break
        elif(e==']'):
            if(len(l)>0 and l[-1]=='['): l.pop()
            else: l.append(e); break
    if(len(l)==0): print('yes')
    else: print('no')