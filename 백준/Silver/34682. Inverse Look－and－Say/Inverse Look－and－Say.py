def f(s):
    q=[]
    r=''
    for e in s:
        if(not q or q[-1]==e): q.append(e); continue
        r+=str(len(q))+q[0]
        q.clear()
        q.append(e)
    if(q):
        r+=str(len(q))+q[0]
    return r

def g(s):
    r=''
    c=0
    for e in s:
        if(c==0): c=int(e)
        else: r+=e*c; c=0
    return r

s=input().strip()
if(f(g(s))==s and g(s)[0]!='0'): print(g(s))
else: print(-1)