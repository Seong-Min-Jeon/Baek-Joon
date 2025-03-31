n,m=map(int,input().split())
s=[]
for i in range(2,int(n**0.5)+1):
    while n%i==0: s.append(i); n//=i
if(n>1): s.append(n)
t={}
for e in s: t[e]=t.get(e,0)+1
M=1000000007
l=[((pow(e,t[e]*m+1,M)-1)*pow(e-1,M-2,M))%M for e in t]
r=1
for e in l: r=(r*e)%M
print(r)