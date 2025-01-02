ip=input
ip()
m=list(map(int,ip().split()))
ip()
n=list(map(int,ip().split()))
l=[]
while True:
    if(len(m)==0 or len(n)==0): break
    if(max(m)==max(n)):
        l.append(max(m))
        m=m[m.index(max(m))+1:]
        n=n[n.index(max(n))+1:]
    else:
        if(max(m)>max(n)): m.remove(max(m))
        else: n.remove(max(n))
print(len(l))
print(*l)