while True:
    a=int(input())
    if(a==0): break
    m,n={},{}
    for _ in range(a):
        x,y,z=input().split()
        x=int(x)
        m[x]=m.get(x,0)+1
        if(z=='Gold'): n[x]=n.get(x,0)+1
    r,t=3000,3000
    for e in n:
        if(n.get(e)>n.get(r,0) or (n.get(e)==n.get(r,0) and r>e)): r=e
    for e in m:
        if(m.get(e)>m.get(t,0) or (m.get(e)==m.get(t,0) and t>e)): t=e
    print(r,t)