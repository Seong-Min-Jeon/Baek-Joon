import sys
i=sys.stdin.readline
l=[]
for _ in range(int(i())):
    c=i()
    if(c.startswith('push')): l.append(c.split()[1])
    elif(c.startswith('pop')): print(l.pop() if len(l)!=0 else -1)
    elif(c.startswith('size')): print(len(l))
    elif(c.startswith('empty')): print(1 if len(l)==0 else 0)
    elif(c.startswith('top')): print(l[-1] if len(l)!=0 else -1)