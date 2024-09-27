import sys
i=sys.stdin.readline
l=[]
for _ in range(int(i())):
    c=i()
    if(c.startswith('push')): l.append(c.split()[1])
    elif(c.startswith('pop')): 
        if(len(l)==0): print(-1); continue
        print(l[0]); del l[0]
    elif(c.startswith('size')): print(len(l))
    elif(c.startswith('empty')): print(1 if len(l)==0 else 0)
    elif(c.startswith('front')): 
        if(len(l)==0): print(-1); continue
        print(l[0])
    elif(c.startswith('back')): 
        if(len(l)==0): print(-1); continue
        print(l[-1])