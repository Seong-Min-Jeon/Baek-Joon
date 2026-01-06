I=input
F=lambda:map(int,I().split())
n,k=F()
l=[]
for i in range(n):
    l+=[(e,i+1) for e in F()]
p=0
q,t=l.pop(0)
while l:
    p=(p+q)%len(l)-1
    if(p<0): p=len(l)-1
    q,t=l.pop(p)
print(t,q)